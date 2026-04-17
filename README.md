# Road-Accident-Analysis


This project is a modular **data pipeline** for analyzing road accident data.
It includes data ingestion, preprocessing, and is designed to scale into a full machine learning pipeline.

---

## 📁 Project Structure

```
project/
│
├── src/
│   ├── components/
│   ├── pipelines/
│   ├── utils/
│   └── config.py
│
├── config.yml
├── template.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### 🔹 Step 2: Activate Environment

#### Windows:

```bash
venv\Scripts\activate
```

#### Mac/Linux:

```bash
source venv/bin/activate
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 4: Create Project Structure

Run the template script to generate required folders and files:

```bash
python template.py
```

---

### 🔹 Step 5: Install Package

```bash
pip install -e .
```

---

## 📥 Data Ingestion

* Dataset is downloaded from Kaggle using API
* Config-driven approach using `config.yml`

---

## 🧹 Data Preprocessing

* Handles missing values
* Removes duplicates
* Feature engineering (e.g., extracting hour from time)

---

## 🚀 Future Work

* Data validation pipeline
* Feature engineering module
* Machine learning model
* Dashboard (Tableau / Streamlit)

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Seaborn / Matplotlib
* Scikit-learn
* Kaggle API

---

## 📌 Notes

* Ensure `kaggle.json` is placed in:

  ```
  C:\Users\<your-username>\.kaggle\
  ```
* Do not upload API keys to GitHub

---

## 👨‍💻 Author

Your Name
Data Science / Data Engineering Enthusiast
