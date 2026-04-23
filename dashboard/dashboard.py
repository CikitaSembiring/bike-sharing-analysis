import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Analysis Dashboard", layout="wide")

# Header Utama
st.title('Proyek Analisis Data: Bike Sharing Dataset 🚲')
st.markdown(f"**Nama:** Cikita Natasya Br Sembiring")
st.markdown("Dashboard ini menampilkan hasil analisis data penyewaan sepeda berdasarkan tren waktu, kondisi cuaca, dan perilaku pengguna.")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    # Menggunakan file yang sudah dibersihkan
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

day_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.header("Filter Tahun")
    selected_year = st.selectbox("Pilih Tahun:", options=day_df['yr'].unique())
    st.markdown("---")
    st.markdown("### Tentang")
    st.write("Analisis ini fokus pada perbedaan perilaku antara pengguna *casual* dan *registered*.")

# Filter data berdasarkan tahun yang dipilih
main_df = day_df[day_df['yr'] == selected_year]

# --- METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    total_all = main_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_all:,}")
with col2:
    total_casual = main_df['casual'].sum()
    st.metric("Total Casual", value=f"{total_casual:,}")
with col3:
    total_registered = main_df['registered'].sum()
    st.metric("Total Registered", value=f"{total_registered:,}")

st.divider()

# --- VISUALISASI 1: TREN BULANAN (Sesuai Pertanyaan Bisnis 1) ---
st.subheader(f"Tren Penyewaan Bulanan di Tahun {selected_year}")
monthly_rent = main_df.groupby('mnth')['cnt'].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=monthly_rent, x='mnth', y='cnt', marker='o', color='#1f77b4', ax=ax1)
ax1.set_xticks(range(1, 13))
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Jumlah Penyewa")
st.pyplot(fig1)

# --- VISUALISASI 2: DAMPAK CUACA (Sesuai Pertanyaan Bisnis 2) ---
st.subheader("Pengaruh Kondisi Cuaca terhadap Pengguna Casual (Hari Libur)")
# Menampilkan rata-rata penyewa casual berdasarkan cuaca pada hari libur
weather_impact = main_df[main_df['holiday'] == 1].groupby('weathersit')['casual'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=weather_impact, x='weathersit', y='casual', palette='viridis', ax=ax2)
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Penyewa Casual")
st.pyplot(fig2)

# --- ANALISIS LANJUTAN: RFM ANALYSIS ---
st.divider()
st.subheader("Analisis Lanjutan: Pertumbuhan Tahunan (RFM - Monetary)")

# Menghitung total per tahun untuk perbandingan (Monetary)
rfm_monetary = day_df.groupby('yr')['cnt'].sum().reset_index()
rfm_monetary.columns = ['Tahun', 'Total Penyewaan (Monetary)']

col_rfm1, col_rfm2 = st.columns([1, 2])
with col_rfm1:
    st.write("Tabel Perbandingan Tahunan:")
    st.dataframe(rfm_monetary)

with col_rfm2:
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.barplot(data=rfm_monetary, x='Tahun', y='Total Penyewaan (Monetary)', palette='magma', ax=ax3)
    st.pyplot(fig3)

st.caption('Copyright (C) Cikita Natasya Br Sembiring 2026')