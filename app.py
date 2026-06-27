import streamlit as st
import pandas as pd

# Konfigurasi halaman utama
st.set_page_config(page_title="Buku Induk Digital", layout="wide")

# Judul Utama Aplikasi
st.markdown("""
    <div style="background-color: #1E3A8A; padding: 20px; border-radius: 10px; margin-bottom: 25px;">
        <h1 style="color: white; text-align: center; margin: 0;">BUKU INDUK & KLAPPER DIGITAL SD</h1>
        <p style="color: #E2E8F0; text-align: center; margin: 5px 0 0 0;">Aplikasi Administrasi Sekolah Dasar</p>
    </div>
""", unsafe_allow_html=True)

# CSS Khusus untuk fitur cetak (mengamankan tampilan saat di-print)
st.markdown("""
    <style>
    @media print {
        [data-testid="stSidebar"], button, header, .stDeployButton, [data-testid="stToolbar"] {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        th, td {
            border: 1px solid black !important;
            padding: 6px !important;
            text-align: left;
        }
        th {
            background-color: #f2f2f2 !important;
            -webkit-print-color-adjust: exact;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi Database Sementara (Session State)
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "nisn", "nis", "nama_lengkap", "jenis_kelamin", "alamat_lengkap", "nama_ayah", "nama_ibu", "kelas_sekarang"
    ])

# MENU UTAMA (SIDEBAR)
st.sidebar.title("MENU")
menu = st.sidebar.selectbox("Pilih Menu:", ["📝 Input Buku Induk", "📥 Import Excel", "🔍 Lihat & Cetak"])

# 1. MENU INPUT DATA
if menu == "📝 Input Buku Induk":
    st.subheader("📝 Input Data Siswa Baru")
    with st.form("form_input"):
        nisn = st.text_input("NISN:")
        nis = st.text_input("NIS:")
        nama_lengkap = st.text_input("NAMA LENGKAP:")
        jenis_kelamin = st.selectbox("JENIS KELAMIN:", ["Laki-laki", "Perempuan"])
        alamat_lengkap = st.text_area("ALAMAT LENGKAP:")
        nama_ayah = st.text_input("NAMA AYAH:")
        nama_ibu = st.text_input("NAMA IBU:")
        kelas_sekarang = st.text_input("KELAS:")
        
        submitted = st.form_submit_button("Simpan Data")
        if submitted:
            new_data = pd.DataFrame([{
                "nisn": nisn, "nis": nis, "nama_lengkap": nama_lengkap, 
                "jenis_kelamin": jenis_kelamin, "alamat_lengkap": alamat_lengkap, 
                "nama_ayah": nama_ayah, "nama_ibu": nama_ibu, "kelas_sekarang": kelas_sekarang
            }])
            st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
            st.success("Data berhasil disimpan!")

# 2. MENU IMPORT EXCEL
elif menu == "📥 Import Excel":
    st.subheader("📥 Import Data dari Excel")
    uploaded_file = st.file_uploader("Pilih file Excel (.xlsx)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            df_excel = pd.read_excel(uploaded_file)
            # Menyamakan nama kolom agar huruf kecil semua
            df_excel.columns = df_excel.columns.str.strip().str.lower().str.replace(" ", "_")
            st.session_state.data = pd.concat([st.session_state.data, df_excel], ignore_index=True)
            st.success("Data Excel berhasil di-import!")
            st.dataframe(df_excel)
        except Exception as e:
            st.error(f"Gagal membaca file Excel. Pastikan format kolom sesuai. Detail: {e}")

# 3. MENU LIHAT & CETAK (YANG LENGKAP)
elif menu == "🔍 Lihat & Cetak":
    st.subheader("🗂️ Cetak Data Buku Induk Lengkap")
    
    if "data" in st.session_state and not st.session_state.data.empty:
        df_tampil = st.session_state.data.copy()
        
        kolom_lengkap = ["nisn", "nis", "nama_lengkap", "jenis_kelamin", "alamat_lengkap", "nama_ayah", "nama_ibu", "kelas_sekarang"]
        kolom_ada = [col for col in kolom_lengkap if col in df_tampil.columns]
        df_tampil = df_tampil[kolom_ada]
        
        nama_kolom_baru = {
            "nisn": "NISN", "nis": "NIS", "nama_lengkap": "NAMA LENGKAP", 
            "jenis_kelamin": "JK", "alamat_lengkap": "ALAMAT LENGKAP", 
            "nama_ayah": "NAMA AYAH", "nama_ibu": "NAMA IBU", "kelas_sekarang": "KELAS"
        }
        df_tampil = df_tampil.rename(columns=nama_kolom_baru)
        
        st.write("### DATA SISWA BUKU INDUK")
        st.markdown(df_tampil.to_html(index=False, escape=False), unsafe_allow_html=True)
        
        st.markdown('<button onclick="window.print()" style="padding: 12px 24px; background-color: #1E3A8A; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 16px;">🖨️ Cetak / Simpan ke PDF</button>', unsafe_allow_html=True)
        st.subheader("🖨️ Tindakan")
        st.markdown('<button onclick="window.print()" style="padding: 12px 24px; background-color: #1E3A8A; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 16px;">🖨️ Cetak / Simpan ke PDF</button>', unsafe_allow_html=True)
    else:
        st.info("Belum ada data Buku Induk yang tersimpan. Silakan input data terlebih dahulu atau import file Excel.")
