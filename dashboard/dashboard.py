import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
main_data = pd.read_csv("dashboard/main_data.csv")  # Gunakan satu dataset utama

# Styling
st.set_page_config(layout="wide")  # Mengatur tampilan agar lebih lebar
st.title("📊 Dashboard Penyewaan Sepeda")

# Sidebar untuk informasi pengguna
with st.sidebar:
    st.image("dashboard/bike.png", width=150)  # Gantilah dengan path logo yang sesuai
    st.subheader("User Information")
    name = st.text_input("Nama", "Muhammad Muttakin")
    cohort_id = st.text_input("Cohort ID", "MC308D5Y2291")
    email = st.text_input("Email", "muttakin2418@gmail.com")

# Layout utama
col1, col2 = st.columns([1, 3])

with col2:
    # 1. Tren jumlah penyewaan sepeda berdasarkan musim
    st.header("🌦️ Tren Penyewaan Berdasarkan Musim")
    seasonal_trend = main_data.groupby("season")["total"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=seasonal_trend.index, y=seasonal_trend.values, palette="viridis", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
    st.pyplot(fig)

    # 2. Perbedaan penyewaan sepeda pada hari kerja dan hari libur
    st.header("📅 Penyewaan Sepeda pada Hari Kerja dan Libur")
    workday_trend = main_data.groupby("workingday")["total"].mean()
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=["Libur", "Hari Kerja"], y=workday_trend.values, palette="coolwarm", ax=ax)
    ax.set_xlabel("Hari")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Perbandingan Penyewaan Sepeda pada Hari Kerja dan Libur")
    st.pyplot(fig)

    # 3. Pola penyewaan sepeda berdasarkan jam dalam sehari
    st.header("⏰ Pola Penyewaan Berdasarkan Jam")
    hourly_trend = main_data.groupby("hour")["total"].mean()
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(x=hourly_trend.index, y=hourly_trend.values, marker="o", color="b", ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Pola Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xticks(range(0,24))
    ax.grid(True)
    st.pyplot(fig)

    # 4. Pengaruh cuaca terhadap jumlah penyewaan sepeda
    st.header("☀️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
    weather_trend = main_data.groupby("weather")["total"].mean()
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=weather_trend.index, y=weather_trend.values, palette="magma", ax=ax)
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    st.pyplot(fig)

    # 5. Clustering Pengguna
    st.header("🔍 Clustering Pengguna")
    main_data['date'] = pd.to_datetime(main_data['date'])
    main_data['day_of_week'] = main_data['date'].dt.dayofweek
    
    def classify_day_based(row):
        return 'Weekend Rider' if row['day_of_week'] in [5, 6] else 'Weekday Rider'
    
    usage_quantiles = main_data['total'].quantile([0.25, 0.75])
    def classify_intensity(row):
        if row['total'] > usage_quantiles[0.75]:
            return 'Heavy User'
        elif row['total'] < usage_quantiles[0.25]:
            return 'Light User'
        else:
            return 'Moderate User'
    
    main_data['Day_Cluster'] = main_data.apply(classify_day_based, axis=1)
    main_data['Usage_Intensity'] = main_data.apply(classify_intensity, axis=1)
    
    day_cluster_counts = main_data['Day_Cluster'].value_counts()
    intensity_cluster_counts = main_data['Usage_Intensity'].value_counts()
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.barplot(x=day_cluster_counts.index, y=day_cluster_counts.values, ax=axes[0], palette='coolwarm')
    axes[0].set_title("Day-Based Clustering")
    axes[0].set_xlabel("Cluster")
    axes[0].set_ylabel("Count")
    
    sns.barplot(x=intensity_cluster_counts.index, y=intensity_cluster_counts.values, ax=axes[1], palette='magma')
    axes[1].set_title("Usage Intensity Clustering")
    axes[1].set_xlabel("Cluster")
    axes[1].set_ylabel("Count")
    
    plt.tight_layout()
    st.pyplot(fig)


