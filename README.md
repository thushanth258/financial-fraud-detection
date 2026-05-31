# Financial Fraud Detection System

## Overview

The Financial Fraud Detection System is a Machine Learning-based web application designed to identify fraudulent financial transactions. The system uses a Random Forest Classifier trained on transaction data and provides predictions through an interactive Streamlit dashboard.

Users can upload transaction datasets and receive fraud detection results along with visual analytics.

---

## Features

- Fraud transaction detection using Machine Learning
- Random Forest Classifier model
- Interactive Streamlit web interface
- Upload transaction datasets in:
  - CSV format
  - Excel (.xlsx) format
  - TXT format
- Fraud and Genuine transaction count
- Bar Chart visualization
- Pie Chart visualization
- User-friendly dashboard

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib

---

## Project Structure

```text
financial-fraud-detection/
│
├── app/
│   └── app.py
│
├── models/
│   └── fraud_model.pkl
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/financial-fraud-detection.git
```

### Navigate to the Project Folder

```bash
cd financial-fraud-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python -m streamlit run app/app.py
```

The application will open in your browser.

---

## How to Use

1. Launch the Streamlit application.
2. Upload a transaction dataset (CSV, XLSX, or TXT).
3. Click **Detect Fraud**.
4. View prediction results.
5. Analyze fraud statistics using charts.

---

## Machine Learning Model

The project uses a **Random Forest Classifier** for fraud detection.

### Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Model Saving using Joblib
8. Deployment with Streamlit

---

## Future Enhancements

- Real-time transaction monitoring
- Deep Learning-based fraud detection
- Advanced dashboard analytics
- Cloud deployment
- User authentication system

---

## Author

Thushanthan R

Panimalar Engineering College, Chennai

---

## License

This project is developed for educational and learning purposes.
