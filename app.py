import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="HackoWeek April Tasks", layout="wide")

st.sidebar.title("April HackoWeek 🚀")
task = st.sidebar.radio("Select Task", [
    "Task 16 - Data Cleaning",
    "Task 17 - Collision Avoidance",
    "Task 18 - Visualization",
    "Task 19 - Social Tracker",
    "Task 20 - Predictive Maintenance"
])

# ---------------- TASK 16 ----------------
if task == "Task 16 - Data Cleaning":
    st.title("📊 Sensor Data Cleaning")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.subheader("Original Data")
        st.write(df)

        cleaned_df = df.fillna(df.mean(numeric_only=True))

        st.subheader("Cleaned Data")
        st.write(cleaned_df)

        st.success("Missing values handled successfully!")

# ---------------- TASK 17 ----------------
elif task == "Task 17 - Collision Avoidance":
    st.title("🚧 Warehouse Collision Avoidance")

    distance = st.slider("Distance from obstacle (cm)", 0, 100, 50)

    if distance < 20:
        st.error("⚠️ Obstacle detected! Slowing down AGV")
    else:
        st.success("✅ Path is clear")

# ---------------- TASK 18 ----------------
elif task == "Task 18 - Visualization":
    st.title("📈 Dataset Visualization")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.write(df.head())

        column = st.selectbox("Select column to visualize", df.columns)

        plt.figure()
        plt.plot(df[column])
        plt.title(f"{column} Trend")

        st.pyplot(plt)

# ---------------- TASK 19 ----------------
elif task == "Task 19 - Social Tracker":
    st.title("📡 Social Interaction Tracker")

    rssi = st.slider("RSSI Value", -100, -20, -60)

    if rssi > -50:
        st.success("Strong Interaction")
    elif rssi > -70:
        st.warning("Medium Interaction")
    else:
        st.error("Weak Interaction")

# ---------------- TASK 20 ----------------
elif task == "Task 20 - Predictive Maintenance":
    st.title("🤖 Predictive Maintenance (ML Model)")

    data = {
        "temperature": [30, 40, 50, 60, 70],
        "vibration": [10, 20, 30, 40, 50],
        "failure": [0, 0, 0, 1, 1]
    }

    df = pd.DataFrame(data)

    X = df[["temperature", "vibration"]]
    y = df["failure"]

    model = LogisticRegression()
    model.fit(X, y)

    temp = st.slider("Temperature", 20, 100, 50)
    vib = st.slider("Vibration", 0, 60, 20)

    prediction = model.predict([[temp, vib]])

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Likely")
    else:
        st.success("✅ Machine is Safe")

st.sidebar.markdown("Made by Harman & Gitika")