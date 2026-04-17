# 🌸  End-to-End Iris Flower Prediction System

A full-stack Machine Learning Web Application that predicts the species of an Iris flower based on its measurements. End-to-end Iris Flower Prediction system using FastAPI, PostgreSQL, and a modern frontend. It predicts flower species from input features, stores results in a database, and allows retrieval/filtering via APIs. Fully integrated ML, backend, database, and UI for real-world deployment.

---
## 🚀 Live Demo [Iris-Flower-Prediction](https://iris-flower-prediction-demo.vercel.app/)

## 🐱‍🏍 Features

- Predict Iris species using ML model
- Store predictions in PostgreSQL
- Retrieve all predictions
- Filter by class (Setosa, Versicolor, Virginica)
- Modern responsive UI

---

## 🧠 ML Model

- Algorithm: Scikit-learn classification model
- Features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Output:
  - Setosa
  - Versicolor
  - Virginica

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL

### Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

End-to-End-IRIS-Flower-Prediction/
│
├── backend/
├── database/
├── frontend/
├── requirements.txt
└── README.md

---

## ⚙️ Setup

1. Clone repo
2. Create virtual environment
3. Install requirements
4. Add .env with DATABASE_URL
5. Run backend:
   uvicorn backend.app:app --reload
6. Open frontend/index.html

---

## 📡 API

POST /predict/
GET /predictions/
GET /class/{class_name}

---

## ⚠️ Fix

If error:
No module named sklearn

Run:
pip install scikit-learn

---
## 🌐 Deployment

### Frontend

* Vercel / Netlify

### Backend

* Render
