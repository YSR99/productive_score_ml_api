# 🚀 Productive Score ML API

An intelligent REST API that predicts a user's daily productivity score based on everyday lifestyle factors. 

## 📖 Project Overview

The **Productive Score ML API** is a machine learning-powered backend service designed to quantify how daily habits impact performance. By analyzing inputs like sleep duration, focus hours, exercise routines, and screen time, the API's trained ML model generates a predicted productivity score. This project bridges the gap between raw data science and accessible software engineering by serving a machine learning model through a robust RESTful interface.

## 🛠️ Tech Stack

This project is built with a focus on modern, efficient, and scalable tools:

* **Backend Framework:** FastAPI (Python)
* **Machine Learning:** scikit-learn
* **Data Processing:** Pandas, NumPy
* **Model Serialization:** joblib

## 🗂️ Project Structure

The repository is organized to separate the machine learning pipeline from the application backend, ensuring clean architecture and easy maintainability:
productive_score_ml_api/
│
├── backend/            # FastAPI application and route definitions
├── src/                # ML training pipeline and feature engineering
├── notebooks/          # Jupyter notebooks for data exploration and experimentation
├── artifacts/          # Serialized models (.pkl / .joblib)
├── data/               # Training datasets and raw data
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
