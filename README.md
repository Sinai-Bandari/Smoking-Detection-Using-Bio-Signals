# Smoking-Detection-Using-Bio-Signals
Machine learning project to detect smoking status from bio-signal data using Python, Flask, and scikit-learn.
Here’s your **updated `README.md`** with a **dataset download section** so you don’t need to upload the large file to GitHub.

---

```markdown
# Smoking Detection Using Bio-Signals

## 📌 Project Overview
This project predicts a person's smoking status based on various **bio-signal health data** using machine learning.  
It includes data preprocessing, visualization, model training, and deployment as a Flask-based web application.

## 🛠 Technologies Used
- **Python** (pandas, NumPy, scikit-learn, seaborn, matplotlib)
- **Flask** (for web app backend)
- **HTML, CSS, JavaScript** (for frontend)
- **Pickle** (for model saving/loading)
- **Git & GitHub** (version control)

## 📂 Project Structure
```

Mini\_project/
│── static/                 # CSS, JS, images
│── templates/              # HTML templates
│── app.py                   # Flask app
│── mini\_project.py          # Data processing & model training
│── model.pkl                # Trained ML model
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation

````

## 📊 Workflow
1. **Data Collection** – Bio-signal dataset  
2. **Data Cleaning** – Handle missing values, outliers  
3. **EDA** – Visualize trends & correlations  
4. **Model Training** – Logistic Regression model  
5. **Model Deployment** – Flask web app for real-time prediction

---

## 📥 Download Dataset
This project uses the **Smoking Status Prediction Dataset** from Kaggle.  
Download it from the link below and place the CSV file in the project folder before running the application:

🔗 [Smoking Status Prediction Dataset – Kaggle](https://www.kaggle.com/datasets/kukuroo3/smoking)


---

## ⚡ Installation & Usage
1. **Clone the repository**
```bash
git clone https://github.com/Sinai-Bandari/Smoking-Detection-Using-Bio-Signals.git
cd Smoking-Detection-Using-Bio-Signals
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Download the dataset** from the link above and place it in the project folder.

4. **Run the Flask app**

```bash
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📌 Example Prediction

* Input: Age, BMI, Pulse Rate, Blood Pressure, CO levels, etc.
* Output: `Smoker` or `Non-Smoker`

---

## 📷 Screenshots

*(Add screenshots of your web app UI here)*
<img width="1533" height="1011" alt="Screenshot 2025-03-31 141016" src="https://github.com/user-attachments/assets/482c099f-d3c0-4fbc-8e3a-94ff4b6184a4" />
<img width="1875" height="720" alt="Screenshot 2025-03-31 141121" src="https://github.com/user-attachments/assets/9ac63527-9350-4f52-ba0b-dd55822eef26" />
<img width="1919" height="887" alt="Screenshot 2025-03-31 141202" src="https://github.com/user-attachments/assets/cbfc08bb-1040-4051-8754-a7108ce406a3" />
<img width="1774" height="997" alt="Screenshot 2025-04-08 202246" src="https://github.com/user-attachments/assets/a83535b9-9b82-4914-98d4-e73f6ca53ec6" />


---

## 📜 License

This project is licensed under the MIT License.

---

### 👤 Author

**Sinai Bandari** – (https://github.com/Sinai-Bandari)

