import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN UTAMA (Wajib di baris paling atas)
st.set_page_config(page_title="PUSDIK - Dashboard SDN Padurenan V", layout="wide", initial_sidebar_state="expanded")

# 2. GAYA CSS PREMIUM & CUSTOM SIDEBAR (Agar mirip 99% dengan Gambar Referensi)
st.markdown("""
    <style>
    /* Mengatur warna latar belakang aplikasi menjadi abu-abu terang sesuai gambar */
    .stApp {
        background-color: #F8FAFC;
    }
    /* Mengatur warna sidebar menjadi gelap sesuai gambar */
    [data-testid="stSidebar"] {
        background-color: #1A1D29 !important;
    }
    /* Sembunyikan elemen bawaan Streamlit yang mengganggu */
    header, footer {visibility: hidden;}
    
    /* Gaya Teks Menu Kategori Sidebar */
    .sidebar-category {
        color: #718096 !important;
        font-size: 11px !important;
        font-weight: bold !important;
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 5px;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOPBAR / HEADER (Tombol Logout & Profil User + Judul Sekolah)
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: white; padding: 10px 20px; border-bottom: 1px solid #E2E8F0; margin-top: -50px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <button style="background-color: #FFF5F5; color: #E53E3E; border: 1px solid #FED7D7; padding: 6px 16px; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 14px;">
                🔄 Logout
            </button>
            <span style="font-weight: bold; color: #2D3748; font-family: sans-serif; font-size: 16px;">SD NEGERI PADURENAN V</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; font-family: sans-serif; color: #4A5568; font-size: 14px;">
            <span>Hi, Admin</span>
            <div style="width: 32px; height: 32px; border-radius: 5px; background-color: #C6F6D5; color: #22543D; display: flex; align-items: center; justify-content: center; font-weight: bold;">
                A
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. DATABASE SEMENTARA (SESSION STATE)
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame([
        {"nisn": "3034930290", "nis": "2025352", "nama_lengkap": "WIIWJFKJW", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Bekasi", "nama_ayah": "WEVWV", "nama_ibu": "QWCFWEQ", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930291", "nis": "2025353", "nama_lengkap": "Budi Santoso", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Bekasi", "nama_ayah": "Slamet", "nama_ibu": "Siti", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930292", "nis": "2025354", "nama_lengkap": "Siti Aminah", "jenis_kelamin": "Perempuan", "alamat_lengkap": "Bekasi", "nama_ayah": "Rahmat", "nama_ibu": "Ani", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930293", "nis": "2019355", "nama_lengkap": "Andi Wijaya", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Bekasi", "nama_ayah": "Tono", "nama_ibu": "Ika", "kelas_sekarang": "Lulus", "tahun_masuk": "2019", "status": "Lulus"}
    ])

# 5. SIDEBAR DENGAN LOGO SEKOLAH DAN STRUKTUR PUSDIK
with st.sidebar:
    # Menampilkan Logo Sekolah (Otomatis background putih kotak bersih rapi di atas Menu)
    st.markdown("""
        <div style="background-color: white; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <img src="https://raw.githubusercontent.com/buku-induk-sd/main/logo%20sekolah%20new.jpeg" onerror="this.src='https://via.placeholder.com/150?text=SDN+PADURENAN+V'" style="width: 100px; height: auto; margin-bottom: 10px;">
            <h5 style="color: #1A1D29; margin: 0; font-size: 12px; font-weight: bold;">SDN PADURENAN V</h5>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: white; font-family: sans-serif; letter-spacing: 3px; margin-bottom: 20px; text-align: center;'>PUSDIK</h2>", unsafe_allow_html=True)
    
    # Navigasi Menu Utama
    st.markdown("<p class='sidebar-category'>DASHBOARD</p>", unsafe_allow_html=True)
    buka_dashboard = st.checkbox("🔷 Dashboard Utama", value=True)
    
    st.markdown("<p class='sidebar-category'>MAIN MENU</p>", unsafe_allow_html=True)
    menu_main = st.selectbox("Menu Utama:", ["- Pilih Data -", "📝 Data Utama (>)", "📊 Data Kelas (>)"], index=0, label_visibility="collapsed")
    
    st.markdown("<p class='sidebar-category'>PENILAIAN</p>", unsafe_allow_html=True)
    menu_nilai = st.selectbox("Penilaian:", ["- Pilih Penilaian -", "📶 Basic Data Setting (>)", "📝 Input Penilaian (>)"], index=0, label_visibility="collapsed")
    
    st.markdown("<p class='sidebar-category'>DOKUMEN DAN BUKU INDUK</p>", unsafe_allow_html=True)
    menu_dokumen = st.selectbox("Dokumen:", ["- Pilih Dokumen -", "📖 Dokumen Siswa (>)", "📋 Lihat & Cetak Buku Induk (>)"], index=0, label_visibility="collapsed")

# Logika Penentu Halaman Aktif (Anti-Error Syntax)
pilihan = "Dashboard"
if "Data Utama" in menu_main: 
    pilihan = "Input"
elif "Data Kelas" in menu_main: 
    pilihan = "Import"
elif "Cetak Buku Induk" in menu_dokumen: 
    pilihan = "Cetak"

# 6. KONTEN HALAMAN UTAMA
if pilihan == "Dashboard":
    st.markdown("<h3 style='color: #4A5568; font-family: sans-serif; font-weight: bold; margin-bottom: 20px;'>DASHBOARD</h3>", unsafe_allow_html=True)
    
    # Kiri (Grafik Batang) & Kanan (Kartu Dashboard)
    kolom_kiri, kolom_kanan = st.columns([6, 5])
    
    with kolom_kiri:
        st.markdown("""
            <div style="background-color: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #E2E8F0; min-height: 420px;">
                <p style="color: #4A5568; font-weight: bold; font-size: 15px; margin-bottom: 25px;">📊 JML Pesdik MTS 10th Terakhir Per Thn Masuk</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Tampilkan Grafik Batang
        df_chart = st.session_state.data.groupby(['tahun_masuk', 'jenis_kelamin']).size().unstack(fill_value=0)
        if not df_chart.empty:
            st.bar_chart(df_chart, height=320)
            
    with kolom_kanan:
        # KARTU GURU (Ungu dan Merah)
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
                <div style="background-color: #9061F9; padding: 25px; border-radius: 15px; color: white; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <div style="font-size: 36px; font-weight: bold; margin-bottom: 5px;">7</div>
                    <div style="font-size: 14px; font-weight: 500; opacity: 0.95;">Guru Aktif</div>
                </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown("""
                <div style="background-color: #F05252; padding: 25px; border-radius: 15px; color: white; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <div style="font-size: 36px; font-weight: bold; margin-bottom: 5px;">1</div>
                    <div style="font-size: 14px; font-weight: 500; opacity: 0.95;">Guru Non Aktif</div>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        
        # KARTU STATUS SISWA (4 Kotak Kecil)
        df_siswa = st.session_state.data
        aktif = len(df_siswa[df_siswa['status'] == 'Aktif'])
        lulus = len(df_siswa[df_siswa['status'] == 'Lulus'])
        pindah = len(df_siswa[df_siswa['status'] == 'Pindah'])
        non_akt = len(df_siswa[df_siswa['status'] == 'Non Aktif'])
        
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.markdown(f'<div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0;"><div style="color: #7C3AED; font-size: 24px; font-weight: bold;">{aktif}</div><div style="color: #94A3B8; font-size: 11px; font-weight: bold;">Aktif</div></div>', unsafe_allow_html=True)
        with col_s2:
            st.markdown(f'<div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0;"><div style="color: #0D9488; font-size: 24px; font-weight: bold;">{lulus}</div><div style="color: #94A3B8; font-size: 11px; font-weight: bold;">Lulus</div></div>', unsafe_allow_html=True)
        with col_s3:
            st.markdown(f'<div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0;"><div style="color: #D97706; font-size: 24px; font-weight: bold;">{pindah}</div><div style="color: #94A3B8; font-size: 11px; font-weight: bold;">Pindah</div></div>', unsafe_allow_html=True)
        with col_s4:
            st.markdown(f'<div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0;"><div style="color: #E11D48; font-size: 24px; font-weight: bold;">{non_akt}</div><div style="color: #94A3B8; font-size: 11px; font-weight: bold;">Non Aktif</div></div>', unsafe_allow_html=True)

# 7. FITUR INPUT DATA Siswa
elif pilihan == "Input":
    st.subheader("📝 Input Data Utama Siswa")
    with st.form("form_input"):
        nisn = st.text_input("NISN:")
        nis = st.text_input("NIS:")
        nama_lengkap = st.text_input("NAMA LENGKAP:")
        jenis_kelamin = st.selectbox("JENIS KELAMIN:", ["Laki-laki", "Perempuan"])
        alamat_lengkap = st.text_area("ALAMAT LENGKAP:")
        nama_ayah = st.text_input("NAMA AYAH:")
        nama_ibu = st.text_input("NAMA IBU:")
        kelas_sekarang = st.text_input("KELAS:")
        tahun_masuk = st.selectbox("TAHUN MASUK:", ["2026", "2025", "2024", "2023", "2022", "2021", "2020"])
        status = st.selectbox("STATUS SISWA:", ["Aktif", "Lulus", "Pindah", "Non Aktif"])
        
        if st.form_submit_button("Simpan"):
            new_data = pd.DataFrame([{"nisn": nisn, "nis": nis, "nama_lengkap": nama_lengkap, "jenis_kelamin": jenis_kelamin, "alamat_lengkap": alamat_lengkap, "nama_ayah": nama_ayah, "nama_ibu": nama_ibu, "kelas_sekarang": kelas_sekarang, "tahun_masuk": tahun_masuk, "status": status}])
            st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
            st.success("Data Berhasil Disimpan!")

# 8. FITUR IMPORT EXCEL
elif pilihan == "Import":
    st.subheader("📥 Import Data Kelas via Excel")
    uploaded_file = st.file_uploader("Upload File Excel", type=["xlsx"])
    if uploaded_file:
        df_excel = pd.read_excel(uploaded_file)
        st.session_state.data = pd.concat([st.session_state.data, df_excel], ignore_index=True)
        st.success("Sukses Import!")

# 9. FITUR LIHAT & CETAK BUKU INDUK (AMBLES AMAN DARI ERROR WINDOW.PRINT)
elif pilihan == "Cetak":
    st.subheader("🗂️ Cetak Data Buku Induk Lengkap")
    df_tampil = st.session_state.data.copy()
    st.dataframe(df_tampil, use_container_width=True)
    
    # Tombol download HTML siap cetak pengganti javascript window.print yang memicu error cloud
    html_table = df_tampil.to_html(index=False)
    html_print = f"<html><head><style>body{{font-family:sans-serif;padding:20px;}}table{{width:100%;border-collapse:collapse;}}th,td{{border:1px solid black;padding:8px;}}th{{background-color:#f2f2f2;}}</style></head><body><h2>DATA BUKU INDUK</h2>{html_table}</body></html>"
    st.download_button(label="🖨️ Unduh File Siap Cetak (HTML)", data=html_print, file_name="buku_induk_sd.html", mime="text/html")

# 10. FOOTER BAWAH PERSIS REFERENSI
st.markdown("<br><br><br>", unsafe_allow_html=True)
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("<p style='color:#A0AEC0; font-size:12px; font-family:sans-serif;'>PUSDIK 201.11</p>", unsafe_allow_html=True)
with col_f2:
    st.markdown("<p style='color:#A0AEC0; font-size:12px; font-family:sans-serif; text-align:right;'>© 2022 ANZFAAM FOUNDATION</p>", unsafe_allow_html=True)
