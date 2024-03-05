import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Add your name and profile picture to the sidebar
st.sidebar.title("User Information")
name = "Fawzul Azhim Mumin"
profile_pic_url = "data:image/jpeg;base64,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"  # URL to your profile picture
st.sidebar.image(profile_pic_url, caption=name, width=150)

# Add a title to the app
st.title("Bike Sharing Analysis Dashboard")

# Add a sidebar for selecting the dataset
dataset_choice = st.sidebar.selectbox("Select Dataset", ["Day", "Hour"])

# Display the selected dataset
if dataset_choice == "Day":
    st.subheader("Day Dataset")
    st.write(day_df.head())
else:
    st.subheader("Hour Dataset")
    st.write(hour_df.head())

# Add a section for data visualization
st.sidebar.subheader("Data Visualization")

# Visualize distribution of target variable 'cnt' in both datasets
if st.sidebar.checkbox("Visualize Distribution of 'cnt'"):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.histplot(data=day_df, x='cnt', ax=axes[0], kde=True)
    axes[0].set_title("Day Dataset - Distribution of 'cnt'")
    sns.histplot(data=hour_df, x='cnt', ax=axes[1], kde=True)
    axes[1].set_title("Hour Dataset - Distribution of 'cnt'")
    st.pyplot(fig)

# Add checkbox options for additional distributions
additional_distributions = st.sidebar.checkbox("Additional Distributions")
if additional_distributions:
    if st.sidebar.checkbox("Visualize Distribution of 'casual'"):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        sns.histplot(data=day_df, x='casual', ax=axes[0], kde=True)
        axes[0].set_title("Day Dataset - Distribution of 'casual'")
        sns.histplot(data=hour_df, x='casual', ax=axes[1], kde=True)
        axes[1].set_title("Hour Dataset - Distribution of 'casual'")
        st.pyplot(fig)

    if st.sidebar.checkbox("Visualize Distribution of 'registered'"):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        sns.histplot(data=day_df, x='registered', ax=axes[0], kde=True)
        axes[0].set_title("Day Dataset - Distribution of 'registered'")
        sns.histplot(data=hour_df, x='registered', ax=axes[1], kde=True)
        axes[1].set_title("Hour Dataset - Distribution of 'registered'")
        st.pyplot(fig)

# Add a section for displaying insights or conclusions
st.sidebar.subheader("Insights/Conclusions")
# Display insights or conclusions based on the analysis
if st.sidebar.checkbox("Show Insights/Conclusions"):
    st.write("Based on the analysis, the following insights and conclusions can be drawn:")
    st.write("- The distribution of 'cnt' (total number of bike rentals) varies between the day and hour datasets.")
    st.write("- The RFM (Recency, Frequency, Monetary) analysis reveals valuable information about customer behavior and transaction patterns.")
    st.write("- Further analysis is recommended to identify trends, patterns, and opportunities for optimization.")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
current_date = day_df['dteday'].max()

rfm_df = day_df.groupby('instant').agg({
    'dteday': lambda x: (current_date - x.max()).days,  # Recency
    'cnt': 'sum',  # Frequency (assuming 'cnt' represents the number of transactions)
    'registered': 'sum'  # Monetary Value (assuming 'registered' represents the monetary value of transactions)
}).rename(columns={'dteday': 'Recency', 'cnt': 'Frequency', 'registered': 'Monetary'})

# Visualize RFM distribution
st.title("RFM Analysis Dashboard")
st.subheader("RFM Distribution")
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
sns.histplot(data=rfm_df, x='Recency', ax=axes[0], kde=True)
axes[0].set_title("Recency Distribution")
sns.histplot(data=rfm_df, x='Frequency', ax=axes[1], kde=True)
axes[1].set_title("Frequency Distribution")
sns.histplot(data=rfm_df, x='Monetary', ax=axes[2], kde=True)
axes[2].set_title("Monetary Distribution")
st.pyplot(fig)

# Display RFM table
st.subheader("RFM Table")
st.write(rfm_df)
