
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Rehab Outcomes Tracker", layout="wide")

st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "Patient Management",
    "Assessment Templates",
    "Performance Tests",
    "Progress Visualization",
    "Reports"
])

patients = pd.DataFrame({
    "Name": ["John Doe", "Jane Smith"],
    "Condition": ["Low Back Pain", "Stroke"],
    "DOB": ["1980-01-01", "1975-06-15"]
})

if section == "Patient Management":
    st.title("Patient Management")
    st.dataframe(patients)
    st.text_input("Add New Patient Name")
    st.date_input("Date of Birth")
    st.selectbox("Condition", patients["Condition"].unique())
    st.text_area("Notes")
    st.button("Save Patient")

elif section == "Assessment Templates":
    st.title("Assessment Templates")
    condition = st.selectbox("Select Condition", patients["Condition"].unique())
    st.subheader(f"Outcome Measures for {condition}")
    if condition == "Low Back Pain":
        st.slider("ODI Score (0-100%)", 0, 100, 40)
        st.slider("NPRS (0-10)", 0, 10, 6)
        st.text_input("PSFS Activities & Scores", "Lifting - 4, Walking - 6")
    elif condition == "Stroke":
        st.slider("Barthel Index (0-100)", 0, 100, 70)
        st.slider("FIM (18-126)", 18, 126, 90)
        st.slider("Berg Balance Scale (0-56)", 0, 56, 40)

elif section == "Performance Tests":
    st.title("Performance-Based Tests")
    test = st.selectbox("Select Test", [
        "Timed Up and Go", "6-Minute Walk Test", "Chair Stand Test",
        "Berg Balance Scale", "Grip Strength", "ROM Measurements"
    ])
    st.number_input("Enter Test Result")
    st.text_area("Observations")
    st.button("Save Test Result")

elif section == "Progress Visualization":
    st.title("Progress Visualization")
    patient = st.selectbox("Select Patient", patients["Name"])
    st.subheader(f"Progress for {patient}")
    progress_data = pd.DataFrame({
        "Week": ["Baseline", "Week 2", "Week 6", "Discharge"],
        "ODI": [60, 50, 40, 30],
        "NPRS": [8, 6, 4, 2]
    })
    fig1 = px.line(progress_data, x="Week", y="ODI", title="ODI Over Time")
    fig2 = px.bar(progress_data, x="Week", y="NPRS", title="NPRS Over Time")
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

elif section == "Reports":
    st.title("Generate Report")
    st.selectbox("Select Patient", patients["Name"])
    st.date_input("Report Date")
    st.text_area("Summary")
    st.button("Export PDF")
