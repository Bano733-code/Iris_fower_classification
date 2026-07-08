# 🌸 Iris Flower Classification Using Machine Learning


## Project Overview

This project uses Machine Learning to classify iris flowers into different species based on their physical measurements.

The model predicts three different species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

The classification is performed using flower features such as:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width


The trained Machine Learning model is deployed as an interactive Streamlit web application.


---

# 🎯 Objectives

The main objectives of this project are:

- Load and analyze the Iris dataset.
- Clean and preprocess the data.
- Select important features.
- Train a classification model.
- Evaluate model performance.
- Build a user-friendly prediction application.


---

# 📂 Project Structure


```
Iris-Flower-Classification
│
├── dataset
│   └── Iris.csv
│
├── iris_model.pkl
├── scaler.pkl
│
├── train.py
├── app.py
├── requirements.txt
└── README.md
```


---

# 📊 Dataset

Dataset:

Iris Flower Dataset


The dataset contains measurements of iris flowers with three classes:

1. Iris-setosa
2. Iris-versicolor
3. Iris-virginica


### Features:

| Feature | Description |
|---|---|
| Sepal Length | Length of sepal in centimeters |
| Sepal Width | Width of sepal in centimeters |
| Petal Length | Length of petal in centimeters |
| Petal Width | Width of petal in centimeters |


### Target:

Flower Species


---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit


---

# 🤖 Machine Learning Model

Algorithm Used:

**Random Forest Classifier**


Why Random Forest?

- Handles classification problems effectively.
- Works well with small datasets.
- Reduces overfitting compared to individual decision trees.
- Provides high prediction accuracy.


---

# 🔄 Project Workflow


## 1. Data Collection

The Iris dataset was collected from Kaggle.


## 2. Data Preprocessing

Steps performed:

- Removed unnecessary columns.
- Checked missing values.
- Separated features and target labels.
- Applied feature scaling.


## 3. Model Training

The dataset was divided into:

- 80% Training Data
- 20% Testing Data


The Random Forest Classifier was trained on the training dataset.


## 4. Model Evaluation

The model was evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix


## 5. Deployment

The trained model was deployed using Streamlit.

Users can enter flower measurements and receive a predicted species with confidence score.


---

# 📈 Model Performance

Evaluation Metrics:

- Accuracy Score
- Precision
- Recall
- F1-score


Example:

```
Accuracy: 96%+
```


---

# 🚀 Installation


Clone the repository:


```
git clone https://github.com/Bano733-code/Iris_fower_classification
```


Install required libraries:


```
pip install -r requirements.txt
```


---

# ▶️ Run the Application


Start Streamlit:


```
streamlit run app.py
```


The application will open in your browser.


---

# 🌸 Application Features

The web application allows users to:

- Enter flower measurements.
- Predict iris species.
- View prediction confidence.


---

# 📸 Screenshots

Add screenshots of:

- Dataset preview
- Data preprocessing
- Model evaluation results
- Confusion matrix
- Streamlit application output


---

# 🔮 Future Improvements

Possible improvements:

- Try advanced classification algorithms.
- Add interactive visualizations.
- Deploy the application online.
- Add a larger flower dataset.


---

# 👩‍💻 Author
Bano Rani

---

# 📌 Conclusion

This project demonstrates how Machine Learning can be used to classify iris flower species accurately. The trained Random Forest model successfully predicts flo
