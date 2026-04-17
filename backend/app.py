from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database.db import SessionLocal, engine
from database.model import Base, Prediction
from database.schemas import PredictionCreate, PredictionResponse
from pickle import load
from pathlib import Path

# Initialize FastAPI app
app = FastAPI(title="Iris Prediction API")

# Enable CORS (for frontend like Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://iris-flower-prediction.netlify.app","https://iris-flower-prediction-demo.vercel.app"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "iris_model.pkl"

try:
    model_data = load(open(MODEL_PATH, "rb"))
    model = model_data["model"]
    classes = model_data["classes"]
except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Health check endpoint
@app.get("/")
def home():
    return {"message": "Iris Prediction API is running 🚀"}


# ✅ Prediction API
@app.post("/predict/", response_model=PredictionResponse)
def predict(prediction: PredictionCreate, db: Session = Depends(get_db)):

    try:
        features = [[
            prediction.sepal_length,
            prediction.sepal_width,
            prediction.petal_length,
            prediction.petal_width
        ]]

        predicted_index = model.predict(features)[0]
        predicted_class = classes[predicted_index]

        db_prediction = Prediction(
            sepal_length=prediction.sepal_length,
            sepal_width=prediction.sepal_width,
            petal_length=prediction.petal_length,
            petal_width=prediction.petal_width,
            predicted_class=predicted_class
        )

        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)

        return db_prediction

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ✅ Get predictions by class
@app.get("/class/{class_name}")
def get_predictions_by_class(class_name: str, db: Session = Depends(get_db)):

    if class_name not in classes:
        raise HTTPException(status_code=404, detail="Class not found")

    results = db.query(Prediction).filter(
        Prediction.predicted_class == class_name
    ).all()

    return results


# ✅ Get all predictions
@app.get("/predictions/")
def get_all_predictions(db: Session = Depends(get_db)):
    return db.query(Prediction).all()
