from pydantic import BaseModel

class PredictionCreate(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    predicted_class: str

    class Config:
        from_attributes = True
