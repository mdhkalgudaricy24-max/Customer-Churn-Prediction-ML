# 📊 Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Acquiring a new customer is significantly more expensive than retaining an existing one. This project predicts whether a customer is likely to churn based on demographic information, subscribed services, contract type, billing details, and account history.

The project is built as a complete end-to-end Machine Learning application that includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, deployment using Flask, and a user-friendly web interface for real-time predictions.

---

# 🎯 Objectives

* Predict whether a customer is likely to churn.
* Compare multiple Machine Learning algorithms.
* Build a production-ready preprocessing pipeline.
* Deploy the trained model as a Flask web application.
* Provide real-time churn predictions with confidence scores.

---

# 🗂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

* **Source:** IBM Sample Dataset
* **Total Records:** 7,043 Customers
* **Features:** 20 Input Features + 1 Target Variable

Target Variable:

* **Churn**

  * Yes
  * No

---

# 📋 Features Used

### Customer Information

* Gender
* Senior Citizen
* Partner
* Dependents

### Account Information

* Tenure
* Contract Type
* Paperless Billing
* Payment Method

### Services

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies

### Billing

* Monthly Charges
* Total Charges

---

# ⚙️ Project Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
Data Preprocessing
      │
      ├── Missing Value Handling
      ├── One-Hot Encoding
      ├── Feature Scaling
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ├── Logistic Regression
      ├── Decision Tree
      ├── Random Forest
      └── XGBoost
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Scikit-learn Pipeline
      │
      ▼
Flask Deployment
      │
      ▼
Real-Time Customer Churn Prediction
```

---

# 🛠 Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* XGBoost

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Deployment

* Flask

### Model Serialization

* Joblib

### Frontend

* HTML5
* CSS3

---

# 🤖 Machine Learning Models Compared

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

---

# 📈 Model Performance

| Model               | Accuracy   |
| ------------------- | ---------- |
| Logistic Regression | **80.38%** |
| XGBoost             | 79.10%     |
| Random Forest       | 78.68%     |
| Decision Tree       | 71.28%     |

**Selected Model:** Logistic Regression

Reason:

* Highest accuracy among evaluated models.
* Fast inference.
* Lightweight model.
* Suitable for deployment using Flask.

---

# 📊 Model Evaluation Metrics

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

# 🌐 Web Application Features

* User-friendly interface
* Real-time prediction
* Confidence score display
* Stay Probability
* Churn Probability
* Responsive design

---

# 📁 Project Structure

```
Customer-Churn-Prediction-ML/

│

├── app.py

├── README.md

├── requirements.txt

├── .gitignore

│

├── dataset/

│      WA_Fn-UseC_-Telco-Customer-Churn.csv

│

├── model/

│      pipeline.pkl

│

├── notebooks/

│      Customer_Churn_ML_Pipeline.ipynb

│

├── static/

│      style.css

│

└── templates/

       index.html
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/mdhkalgudaricy24-max/Customer-Churn-Prediction-ML.git
```

Move into the project folder

```bash
cd Customer-Churn-Prediction-ML
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```


---

# 💡 Future Improvements

* Deploy on Render or Railway
* Add SHAP Explainability
* Dockerize the application
* Add user authentication
* Batch prediction using CSV upload
* Interactive dashboard with Plotly

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing
* Feature Engineering
* Exploratory Data Analysis
* Model Selection
* Model Evaluation
* Scikit-learn Pipelines
* Flask Deployment
* Git & GitHub
* End-to-End Machine Learning Workflow

---

# 👨‍💻 Author

**Mohammad Hasanabasha Kalgudari**

Computer Science Engineering (Cyber Security)

RV College of Engineering

Bengaluru, India

#
