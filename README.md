# Cybersecurity Log Classifier

## Overview

This project demonstrates the integration of a machine learning model into a cybersecurity monitoring system.

A Random Forest Classification model is trained using simulated cybersecurity event data and is then integrated into a standalone inference application capable of classifying events as either:

- Normal
- Suspicious

The project demonstrates dataset generation, model training, model evaluation, model persistence, and inference using Python and Scikit-Learn.

---

## Problem Statement

Security teams process large volumes of log data and must rapidly identify potentially suspicious activity.

This project explores how machine learning can be used to classify cybersecurity events based on common indicators such as failed login attempts, out-of-hours access, and large file downloads.

---

## Features

- Generate cybersecurity log datasets
- Train a machine learning classification model
- Evaluate model performance
- Save a trained model for reuse
- Load and run the model in a separate application
- Classify security events as Normal or Suspicious

---

## Technologies Used

- Python 3.12
- Pandas
- Scikit-Learn
- Joblib
- Git
- GitHub

---

## Dataset Features

The model uses the following cybersecurity indicators:

| Feature | Description |
|----------|-------------|
| failed_logins | Number of failed login attempts |
| off_hours_login | Login occurred outside normal business hours (0 = No, 1 = Yes) |
| file_download_mb | Size of downloaded data in MB |

Target classifications:

- Normal
- Suspicious

---

## Project Structure

```text
cyber-log-classifier/

├── data/
│   └── logs.csv

├── models/
│   └── model.pkl

├── generate_logs.py
├── train_model.py
├── predict_log.py

├── requirements.txt
└── README.md
```

---

## Machine Learning Approach

The model is trained using labelled cybersecurity events and learns relationships between:

- Failed login activity
- Out-of-hours system access
- Download volume

The trained model predicts whether a new event should be classified as Normal or Suspicious.

---

## Model Training

Generate sample data:

```bash
python generate_logs.py
```

Train the model:

```bash
python train_model.py
```

Example output:

```text
Model Accuracy: 100.00%
Model saved successfully.
```

The model is automatically saved to:

```text
models/model.pkl
```

---

## Running Inference

Run the inference application:

```bash
python predict_log.py
```

Example:

```text
Failed Login Attempts: 15
Off Hours Login (0 = No, 1 = Yes): 1
File Download Size (MB): 800

Classification: Suspicious
```

Example:

```text
Failed Login Attempts: 2
Off Hours Login (0 = No, 1 = Yes): 0
File Download Size (MB): 100

Classification: Normal
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JaC-stac-source/cyber-log-classifier.git
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Skills Demonstrated

- Machine Learning
- Python Programming
- Data Processing
- Model Training
- Model Evaluation
- Classification Algorithms
- Cybersecurity Analytics
- Git Version Control
- GitHub Documentation
