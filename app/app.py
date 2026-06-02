import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# Load Model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "fraud_model.pkl"
)

model = joblib.load(model_path)
st.markdown("""
<style>
.stApp {
    background-color: #0B0B0B;
}
</style>
""", unsafe_allow_html=True)

st.title("Financial Fraud Detection System")

uploaded_file = st.file_uploader(
    "Upload Transaction Dataset",
    type=["csv", "xlsx", "txt"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    elif uploaded_file.name.endswith(".txt"):
        df = pd.read_csv(uploaded_file, delimiter=",")

    st.subheader("Uploaded Data")
    st.write(df.head())

    if st.button("Detect Fraud"):

        if "Class" in df.columns:
            df = df.drop("Class", axis=1)

        predictions = model.predict(df)

        df["Prediction"] = predictions

        st.subheader("Prediction Results")
        st.write(df)

        fraud_count = (df["Prediction"] == 1).sum()
        genuine_count = (df["Prediction"] == 0).sum()

        st.metric("Fraud Transactions", fraud_count)
        st.metric("Genuine Transactions", genuine_count)

        # Bar Chart
                # Bar Chart
        chart_data = pd.DataFrame({
            "Type": ["Fraud", "Genuine"],
            "Count": [fraud_count, genuine_count]
        })

        st.subheader("Fraud vs Genuine Transactions (Bar Chart)")

        fig_bar, ax_bar = plt.subplots()

        ax_bar.bar(
            ["Fraud", "Genuine"],
            [fraud_count, genuine_count],
            color=["#00BFFF", "#6A0DAD"]
        )

        ax_bar.set_facecolor("#0B0B0B")
        fig_bar.patch.set_facecolor("#0B0B0B")

        ax_bar.tick_params(colors="white")
        ax_bar.title.set_color("white")
        ax_bar.set_title("Fraud vs Genuine Transactions")

        st.pyplot(fig_bar)

        # Pie Chart
        st.subheader("Fraud vs Genuine Transactions (Pie Chart)")

        fig, ax = plt.subplots()

        ax.pie(
            [fraud_count, genuine_count],
            labels=["Fraud", "Genuine"],
            colors=["#00BFFF", "#6A0DAD"],
            autopct="%1.1f%%",
            startangle=90,
            explode=(0.08, 0)
        )

        ax.axis("equal")
        fig.patch.set_facecolor("#0B0B0B")

        st.pyplot(fig)