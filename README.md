# 📈 Student Marks Predictor

## 1. Project Overview 🎯

This project provides an end-to-end solution for predicting student academic marks based on their study hours. It integrates a machine learning model developed through detailed data analysis with a user-friendly web application, making the prediction readily accessible. The aim is to offer insights into the relationship between study effort and performance.

## 2. Key Features ✨

* **Data Analysis & Model Training**: Comprehensive Jupyter Notebook (`Student Marks Predictor.ipynb`) for Exploratory Data Analysis (EDA), data preprocessing, and training a regression model to predict student marks.
* **Web Application Interface**: A Flask-based web application (`app.py`) that serves as an intuitive interface for users to input study hours and receive instant mark predictions.
* **Input Validation**: Ensures robust user input by validating study hours (0-24 hours).
* **Model Persistence**: The trained machine learning model is saved and loaded efficiently using `joblib`, ensuring the application uses a consistent, pre-trained model.

## 3. Tech Stack Used 🛠️

* **Programming Language**: Python 🐍
* **Web Framework**: Flask 🌐
* **Data Manipulation**: `pandas`, `numpy`
* **Machine Learning**: `scikit-learn` (for model training)
* **Model Serialization**: `joblib`
* **Data Visualization**: `matplotlib` (primarily for analysis in the notebook) 📊
* **Development Environment**: Jupyter Notebook 📓

## 4. How to Run the Project ▶️

Follow these steps to set up and run the Student Marks Predictor locally:

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/YourUsername/Student-Marks-Predictor.git](https://github.com/YourUsername/Student-Marks-Predictor.git)
    cd Student-Marks-Predictor
    ```
    *(Note: Replace `YourUsername` with your actual GitHub username or the repository's path)*

2.  **Install Dependencies**:
    It's highly recommended to use a virtual environment.
    ```bash
    pip install Flask joblib numpy pandas scikit-learn matplotlib
    ```

3.  **Model File**:
    Ensure the trained model file, `student_mark_predictor.pkl`, is present in the root directory (same location as `app.py`). This file is generated when the Jupyter notebook is executed and the model is saved.

4.  **Run the Flask Application**:
    ```bash
    python app.py
    ```
    Open your web browser and navigate to the address shown in your terminal (usually `http://127.0.0.1:5000/`).

## 5. Model Inputs ⚙️

The web application's prediction model primarily takes one input:

* **`Study Hours`**: The number of hours a student has studied (expected as an integer between 0 and 24).

## 6. Insights and Outcomes 💡

* **Quantitative Performance Prediction**: Provides a data-driven estimation of student marks based on study duration.
* **Understanding Correlation**: The analysis in the Jupyter Notebook helps visualize and understand the correlation between study hours and academic performance.
* **Educational Tool**: Can serve as a simple tool for students to understand the potential impact of their study efforts.
* **Practical ML Deployment**: Demonstrates a basic, yet complete, pipeline for deploying a machine learning model as a web service.
