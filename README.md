# Cybersecurity Log Classifier

## Overview

This uni project demonstrates the integration of a machine learning model into a cybersecurity monitoring system.

A Random Forest Classification model is trained using simulated security log data and used to classify events as either:

- Normal
- Suspicious

The project includes dataset generation, model training, model evaluation, and a standalone inference application.

---

## Features

- Generate cybersecurity log datasets
- Train a machine learning classification model
- Evaluate model accuracy
- Save trained models using Joblib
- Load and use a trained model for inference
- Classify suspicious cybersecurity events

---

## Technologies

- Python 3.12
- Pandas
- Scikit-Learn
- Joblib

---

## Dataset Features

The model is trained using the following security event attributes:

- Failed Login Attempts
- Off-Hours Login Activity
- File Download Size (MB)

The target classification is:

- Normal
- Suspicious

---

## Project Structure