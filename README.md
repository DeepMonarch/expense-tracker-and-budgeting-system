
### ML-Powered Expense Tracker & Intelligent Budgeting System

It is a full-stack financial intelligence system built using **FastAPI, Streamlit, and Machine Learning**.  
It automatically categorizes expenses, visualizes spending behavior, and lays the foundation for predictive budgeting and anomaly detection.

---

## 🚀 Features

### 🧠 Intelligent Expense Categorization
- NLP-based categorization (TF-IDF + Logistic Regression)
- Rule-based fallback system (cold start solution)
- Expandable retraining pipeline

### 📊 Interactive Financial Dashboard
- Category breakdown (Pie Chart)
- Spending comparison (Bar Chart)
- Real-time expense updates
- Clean SaaS-style UI built with Streamlit

### 🏗 Clean Backend Architecture
- FastAPI REST API
- SQLAlchemy ORM
- Pydantic validation
- Modular structure (models, schemas, ml, database)

### 🗄 Database
- SQLite (development)
- Designed for PostgreSQL migration (production-ready)

---

## 🏛 System Architecture

Streamlit Frontend
↓
FastAPI Backend (REST API)
↓
ML Categorization Layer
↓
SQLite / PostgreSQL Database


---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Isolation Forest (anomaly detection ready)

### Frontend
- Streamlit
- Plotly

### Deployment
- Render (Backend)
- Streamlit Cloud / Render (Frontend)

---

## 📂 Project Structure

smart-finance-ai/
│
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── ml.py
│ └── requirements.txt
│
├── frontend/
│ └── app.py
│
└── README.md


---

## ⚙️ API URL:
https://expense-tracker-and-budgeting-system.onrender.com/

## Streamlit app:
https://expense-tracker-and-budgeting-system.streamlit.app/

