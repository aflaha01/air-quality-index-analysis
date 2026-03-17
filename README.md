# AQI Prediction Web App

This project is a **Machine Learning web application** that predicts the **Air Quality Index (AQI)** using environmental pollutant data.
The model was trained using **Random Forest** and deployed with **Flask**.

---

## Features

* Predicts Air Quality Index (AQI)
* Machine Learning model using Random Forest
* Flask web application
* Simple dashboard-style interface

---

## Project Structure

```
AQI/
│
├── models/
│   ├── aqi_random_forest_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   └── data_analysis.ipynb
│
├── static/
│   ├── css/style.css
│   └── js/script.js
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```


## Installation

Clone the repository:

```bash
git clone https://github.com/aflaha01/AQI.git
cd AQI
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML / CSS / JavaScript
* Jupyter Notebook

---

## Author

https://github.com/aflaha01
