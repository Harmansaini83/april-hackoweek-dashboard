# 🚀 April HackoWeek Dashboard  
### IoT + Data Analytics + Machine Learning using Streamlit

---

## 📌 Project Overview

The **April HackoWeek Dashboard** is an interactive web-based application developed using Streamlit that demonstrates real-world applications of Internet of Things (IoT), data analytics, and machine learning.

This project simulates multiple industrial and smart-system scenarios such as:
- Sensor data preprocessing
- Collision detection systems
- Human interaction tracking
- Predictive maintenance using ML

The application is designed to provide a simple, user-friendly interface where users can interact with data and visualize results in real-time.

---

## 🎯 Objectives

- To build an interactive dashboard using Python and Streamlit  
- To simulate real-world IoT use cases without physical hardware  
- To perform data cleaning and preprocessing on sensor datasets  
- To visualize time-series data effectively  
- To implement a basic machine learning model for predictive analysis  

---

## 🧠 Problem Statement

In modern industries and smart environments, systems rely heavily on sensor data for decision-making. However, challenges include:
- Handling incomplete or missing sensor data  
- Detecting obstacles in automated environments  
- Understanding human interaction using signals  
- Predicting machine failures before they occur  

This project addresses these challenges through simulation and data-driven solutions.

---

## ⚙️ System Architecture
User Input (UI)
↓
Streamlit Interface
↓
Data Processing (Pandas)
↓
Visualization (Matplotlib)
↓
Machine Learning Model (Scikit-learn)
↓
Output Display (Dashboard)

---

## 🧩 Modules / Tasks Implemented

---

### 🔹 Task 16: Sensor Data Cleaning

#### 📌 Description:
This module handles raw sensor data that may contain missing or null values.

#### ⚙️ Functionality:
- Upload CSV file
- Detect missing values
- Replace missing values with mean (numerical columns)
- Display cleaned dataset

#### 🛠️ Tools Used:
- Pandas

---

### 🔹 Task 17: Warehouse Collision Avoidance

#### 📌 Description:
Simulates an automated guided vehicle (AGV) system that avoids collisions using proximity sensing.

#### ⚙️ Functionality:
- User inputs distance using slider
- If distance < threshold → Alert generated
- Else → Safe condition displayed

#### 🧠 Logic:
- Threshold-based decision system

---

### 🔹 Task 18: Data Visualization

#### 📌 Description:
Visualizes sensor data trends using graphical representation.

#### ⚙️ Functionality:
- Upload dataset
- Select column dynamically
- Generate time-series plot

#### 🛠️ Tools Used:
- Matplotlib

---

### 🔹 Task 19: Social Interaction Tracker

#### 📌 Description:
Simulates human interaction detection using RSSI (Received Signal Strength Indicator).

#### ⚙️ Functionality:
- Input RSSI value
- Classify interaction strength:
  - Strong
  - Medium
  - Weak

#### 🧠 Use Case:
- Contact tracing
- Smart environments

---

### 🔹 Task 20: Predictive Maintenance (Machine Learning)

#### 📌 Description:
Predicts machine failure based on sensor inputs using a classification model.

#### ⚙️ Functionality:
- Uses temperature and vibration data
- Applies Logistic Regression model
- Predicts:
  - Failure likely
  - System safe

#### 🛠️ Tools Used:
- Scikit-learn

---

## 🛠️ Tech Stack

| Technology | Purpose |
|----------|--------|
| Python | Core Programming |
| Streamlit | Web Application Framework |
| Pandas | Data Handling |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |

---

## 📂 Project Structure
aprilhackoweek/
│── app.py # Main Streamlit application
│── sensor_data.csv # Sample dataset
│── README.md # Documentation
│── screenshots/ # Output images


---

## 📊 Sample Dataset

The project uses a sample CSV file containing:
- Time-series data
- Temperature readings
- Vibration values
- Proximity sensor data

Missing values are intentionally included for testing data cleaning functionality.

---

---

## 💡 Key Features

- Interactive UI with sidebar navigation  
- Real-time data processing  
- Dynamic graph generation  
- Machine learning integration  
- Beginner-friendly implementation  

---

## 📚 Key Learnings

- Building web apps using Streamlit  
- Handling missing data using Pandas  
- Data visualization techniques  
- Implementing machine learning models  
- Designing modular applications  

---

## 🚀 Future Enhancements

- Integration with real IoT sensors  
- Deployment on cloud platforms  
- Advanced machine learning models  
- Database integration  
- Improved UI/UX design  

---

## 🎤 Use Cases

- Smart factories  
- Industrial automation  
- Health monitoring systems  
- Smart city applications  
- AI-based monitoring systems  

---

## 👨‍💻 Author

**Harman Saini**  
B.Tech CSE (AIML)  


---

## ⭐ Support

If you found this project useful:
- Give it a ⭐ on GitHub  
- Share with others  
- Connect for collaboration  

---

## 📜 License

This project is for educational purposes.
