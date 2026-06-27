import streamlit as st
import pandas as pd
import numpy as np

# ==============================================================================
# 1. KONFIGURASI HALAMAN UTAMA (Wajib diletakkan di paling atas)
# ==============================================================================
st.set_page_config(
    page_title="PUSDIK - SDN Padurenan V",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. GAYA CSS PREMIUM CUSTOM (Dashboard & Cetak Professional)
# ==============================================================================
st.markdown("""
    <style>
    /* Latar belakang aplikasi utama */
    .stApp {
        background-color: #F8FAFC;
    }
    /* Warna Gelap Sidebar Utama */
    [data-testid="stSidebar"] {
        background-color: #1A1D29 !important;
    }
    /* Menyembunyikan elemen bawaan Streamlit yang kurang rapi */
    header, footer {visibility: hidden;}
    
    /* Judul Kategori Sidebar */
    .sidebar-category {
        color: #64748B !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px;
        margin-top: 25px;
        margin-bottom: 8px;
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
    }
    
    /* Kartu Dashboard Besar (Guru Aktif / Non Aktif) */
    .card-purple {
        background: linear-gradient(135deg, #7C3AED 0%, #9333EA 100%);
        padding: 24px;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 15px -3px rgba(124, 58, 237, 0.2);
        font-family: 'Inter', sans-serif;
        margin-bottom: 15px;
    }
    .card-red {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        padding: 24px;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.2);
        font-family: 'Inter', sans-serif;
        margin-bottom: 15px;
    }
    
    /* Kartu Mini Status Siswa */
    .mini-card {
        background-color: white;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    
    /* Teks dan Kontainer khusus Klapper & Buku Induk */
    .buku-induk-header {
        background-color: #1E3A8A;
        color: white;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Mengatur Gaya Tabel agar Terlihat Premium */
    .dataframe {
        border-collapse: collapse !important;
        width: 100% !important;
    }
    .dataframe th {
        background-color: #1A1D29 !important;
        color: white !important;
        padding: 12px !important;
        text-align: left !important;
    }
    .dataframe td {
        padding: 10px !important;
        border-bottom: 1px solid #E2E8F0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. KEPALA HALAMAN (TOPBAR / HEADER)
# ==============================================================================
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: white; padding: 12px 24px; border-bottom: 1px solid #E2E8F0; margin-top: -55px; margin-bottom: 25px; border-radius: 0 0 8px 8px;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="background-color: #FFF5F5; color: #E53E3E; border: 1px solid #FED7D7; padding: 6px 16px; border-radius: 6px; font-weight: bold; font-size: 13px; cursor: pointer;">
                🔴 Logout
            </span>
            <div style="width: 2px; height: 20px; background-color: #E2E8F0;"></div>
            <span style="font-weight: 700; color: #1E293B; font-size: 15px; letter-spacing: 0.5px;">SD NEGERI PADURENAN V</span>
        </div>
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="color: #64748B; font-size: 14px; font-weight: 500;">Hi, Admin</span>
            <div style="width: 34px; height: 34px; border-radius: 8px; background-color: #CCFBF1; color: #0F766E; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px;">
                A
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. DATABASE UTAMA SISWA (Menggunakan Session State agar Data Bersifat Dinamis)
# ==============================================================================
if "siswa_db" not in st.session_state:
    st.session_state.siswa_db = pd.DataFrame([
        {"NISN": "3034930290", "NIS": "2025352", "Nama Lengkap": "ADITYA PRATAMA", "JK": "Laki-laki", "Kelas": "3A", "Tahun Masuk": "2024", "Abjad Klapper": "A", "Status": "Aktif", "Tempat Lahir": "Bekasi", "Tanggal Lahir": "2015-04-12", "Alamat": "Padurenan Jaya No. 12"},
        {"NISN": "3034930291", "NIS": "2025353", "Nama Lengkap": "ALICIA PUTRI", "JK": "Perempuan", "Kelas": "3A", "Tahun Masuk": "2024", "Abjad Klapper": "A", "Status": "Aktif", "Tempat Lahir": "Jakarta", "Tanggal Lahir": "2015-08-20", "Alamat": "Mustika Jaya Residence"},
        {"NISN": "3034930292", "NIS": "2025354", "Nama Lengkap": "BUDI SANTOSO", "JK": "Laki-laki", "Kelas": "4B", "Tahun Masuk": "2023", "Abjad Klapper": "B", "Status": "Aktif", "Tempat Lahir": "Bekasi", "Tanggal Lahir": "2014-01-05", "Alamat": "Bantargebang RT 02/01"},
        {"NISN": "3034930293", "NIS": "2025355", "Nama Lengkap": "CHELSEA OLIVIA", "JK": "Perempuan", "Kelas": "6A", "Tahun Masuk": "2020", "Abjad Klapper": "C", "Status": "Lulus", "Tempat Lahir": "Bandung", "Tanggal Lahir": "2012-11-15", "Alamat": "Kec. Mustikajaya, Bekasi"},
        {"NISN": "3034930294", "NIS": "2025356", "Nama Lengkap": "DANIEL WIJAYA", "JK": "Laki-laki", "Kelas": "5A", "Tahun Masuk": "2022", "Abjad Klapper": "D", "Status": "Pindah", "Tempat Lahir": "Bekasi", "Tanggal Lahir": "2013-05-30", "Alamat": "Perumahan Padurenan Indah"},
    ])

# ==============================================================================
# 5. STRUKTUR SIDEBAR (Logo Sekolah Bersih + Menu Navigasi PUSDIK)
# ==============================================================================
with st.sidebar:
    # Kontainer Logo Sekolah dengan bingkai putih bersih elegan
    st.markdown("""
        <div style="background-color: white; padding: 16px; border-radius: 12px; text-align: center; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.1);">
            <img src="https://raw.githubusercontent.com/buku-induk-sd/main/logo%20sekolah%20new.jpeg" onerror="this.src='https://via.placeholder.com/120?text=SDN+PADURENAN+V'" style="width: 85px; height: auto; margin-bottom: 8px;">
            <h6 style="color: #1A1D29; margin: 0; font-size: 12px; font-weight: 700; letter-spacing: 0.5px;">SDN PADURENAN V</h6>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: white; font-family: sans-serif; letter-spacing: 4px; margin-bottom: 25px; text-align: center; font-size: 22px; font-weight: 800;'>PUSDIK</h2>", unsafe_allow_html=True)
    
    # KATEGORI 1: DASHBOARD
    st.markdown("<p class='sidebar-category'>Dashboard</p>", unsafe_allow_html=True)
    buka_dashboard = st.checkbox("📊 Dashboard Utama", value=True)
    
    # KATEGORI 2: MAIN MENU
    st.markdown("<p class='sidebar-category'>Main Menu</p>", unsafe_allow_html=True)
    menu_main = st.selectbox(
        "Menu Administrasi:",
        ["- Pilih Menu Utama -", "📖 Buku Induk Siswa (>)", "🗂️ Klapper Digital (>)", "📝 Input Data Baru (>)"],
        index=0, label_visibility="collapsed"
    )
    
    # KATEGORI 3: PENILAIAN
    st.markdown("<p class='sidebar-category'>Penilaian</p>", unsafe_allow_html=True)
    menu_nilai = st.selectbox(
        "Menu Nilai:",
        ["- Pilih Penilaian -", "📶 Basic Data Setting (>)", "📝 Input Penilaian (>)"],
        index=0, label_visibility="collapsed"
    )
    
    # KATEGORI 4: DOKUMEN DAN CETAK
    st.markdown("<p class='sidebar-category'>Dokumen</p>", unsafe_allow_html=True)
    menu_dokumen = st.selectbox(
        "Menu Cetak:",
        ["- Pilih Dokumen -", "📋 Cetak Buku Induk (>)", "📋 Cetak Lembar Klapper (>)"],
        index=0, label_visibility="collapsed"
    )

# Menentukan Halaman Aktif berdasarkan pilihan Dropdown/Checkbox
page_active = "Dashboard"
if "Buku Induk" in menu_main:
    page_active = "Buku Induk"
elif "Klapper Digital" in menu_main:
    page_active = "Klapper"
elif "Input Data Baru" in menu_main:
    page_active = "Input"
elif "Cetak" in menu_dokumen:
    page_active = "Cetak"

# ==============================================================================
# 6. KONTEN HALAMAN: DASHBOARD UTAMA
# ==============================================================================
if page_active == "Dashboard":
    st.markdown("<h3 style='color: #334155; font-weight: 700; margin-bottom: 20px;'>DASHBOARD UTAMA</h3>", unsafe_allow_html=True)
    
    col_graph, col_cards = st.columns([6, 5])
    
    with col_graph:
        st.markdown("""
            <div style="background-color: white; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0; min-height: 410px;">
                <p style="color: #475569; font-weight: 700; font-size: 14px; margin-bottom: 20px;">📊 JML Pesdik Sekolah 10th Terakhir Per Thn Masuk</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Grafik batang interaktif pengelompokan jenis kelamin & tahun masuk siswa
        df_chart_data = st.session_state.siswa_db.groupby(['Tahun Masuk', 'JK']).size().unstack(fill_value=0)
        if not df_chart_data.empty:
            st.bar_chart(df_chart_data, height=310)
            
    with col_cards:
        # Bagian Atas: Info Guru Terbuka Persis Foto Referensi
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
                <div class="card-purple">
                    <div style="font-size: 38px; font-weight: 800; margin-bottom: 2px;">7</div>
                    <div style="font-size: 13px; font-weight: 600; opacity: 0.9;">👨‍🏫 Guru Aktif</div>
                </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown("""
                <div class="card-red">
                    <div style="font-size: 38px; font-weight: 800; margin-bottom: 2px;">1</div>
                    <div style="font-size: 13px; font-weight: 600; opacity: 0.9;">🚫 Guru Non Aktif</div>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
        
        # Bagian Bawah: 4 Kotak Mini Status Siswa Aktual
        df_s = st.session_state.siswa_db
        total_aktif = len(df_s[df_s['Status'] == 'Aktif'])
        total_lulus = len(df_s[df_s['Status'] == 'Lulus'])
        total_pindah = len(df_s[df_s['Status'] == 'Pindah'])
        total_non = len(df_s[df_s['Status'] == 'Non Aktif'])
        
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.markdown(f'<div class="mini-card"><div style="color: #7C3AED; font-size: 24px; font-weight: 800;">{total_aktif}</div><div style="color: #64748B; font-size: 11px; font-weight: bold; margin-top:4px;">Aktif</div></div>', unsafe_allow_html=True)
        with col_s2:
            st.markdown(f'<div class="mini-card"><div style="color: #0D9488; font-size: 24px; font-weight: 800;">{total_lulus}</div><div style="color: #64748B; font-size: 11px; font-weight: bold; margin-top:4px;">Lulus</div></div>', unsafe_allow_html=True)
        with col_s3:
            st.markdown(f'<div class="mini-card"><div style="color: #D97706; font-size: 24px; font-weight: 800;">{total_pindah}</div><div style="color: #64748B; font-size: 11px; font-weight: bold; margin-top:4px;">Pindah</div></div>', unsafe_allow_html=True)
        with col_s4:
            st.markdown(f'<div class="mini-card"><div style="color: #E11D48; font-size: 24px; font-weight: 800;">{total_non}</div><div style="color: #64748B; font-size: 11px; font-weight: bold; margin-top:4px;">Non Aktif</div></div>', unsafe_allow_html=True)

# ==============================================================================
# 7. KONTEN HALAMAN: BUKU INDUK DIGITAL
# ==============================================================================
elif page_active == "Buku Induk":
    st.markdown("""
        <div class="buku-induk-header">
            <h2 style='margin: 0; font-weight: 800; font-size: 24px; letter-spacing: 0.5px;'>📖 BUKU INDUK SISWA DIGITAL</h2>
            <p style='margin: 5px 0 0 0; opacity: 0.8; font-size: 14px;'>SD NEGERI PADURENAN V</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Kontrol filter pencarian cepat multi-kolom
    col_f1, col_f2 = st.columns([8, 4])
    with col_f1:
        cari_nama = st.text_input("🔍 Cari Berdasarkan Nama Lengkap Siswa:")
    with col_f2:
        pilih_status = st.selectbox("Status Keaktifan:", ["Semua Status", "Aktif", "Lulus", "Pindah"])
        
    # Proses penyaringan data tabel
    df_filtered = st.session_state.siswa_db.copy()
    if cari_nama:
        df_filtered = df_filtered[df_filtered['Nama Lengkap'].str.contains(cari_nama.upper(), na=False)]
    if pilih_status != "Semua Status":
        df_filtered = df_filtered[df_filtered['Status'] == pilih_status]
        
    st.dataframe(df_filtered, use_container_width=True)

# ==============================================================================
# 8. KONTEN HALAMAN: KLAPPER DIGITAL (Urutan Abjad & Nama)
# ==============================================================================
elif page_active == "Klapper":
    st.markdown("""
        <div style="background-color: #0F766E; color: white; padding: 25px; border-radius: 12px; text-align: center; margin-bottom: 25px;">
            <h2 style='margin: 0; font-weight: 800; font-size: 24px;'>🗂️ KLAPPER ADMINISTRASI DIGITAL</h2>
            <p style='margin: 5px 0 0 0; opacity: 0.8; font-size: 14px;'>Penyusunan Daftar Siswa Berdasarkan Urutan Abjad Huruf A-Z</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Pemilihan huruf abjad klapper
    abjad_pilihan = st.radio(
        "Pilih Indeks Huruf Abjad Klapper:",
        ["Semua", "A", "B", "C", "D", "E", "F", "G", "H"],
        horizontal=True
    )
    
    df_klapper = st.session_state.siswa_db.copy()
    if abjad_pilihan != "Semua":
        df_klapper = df_klapper[df_klapper['Abjad Klapper'] == abjad_pilihan]
        
    # Urutkan secara Alphabetis otomatis
    df_klapper = df_klapper.sort_values(by="Nama Lengkap")
    
    # Menampilkan tabel khusus format Klapper (termasuk Tempat & Tanggal Lahir)
    st.dataframe(
        df_klapper[["Abjad Klapper", "Nama Lengkap", "JK", "NIS", "NISN", "Tempat Lahir", "Tanggal Lahir", "Status"]],
        use_container_width=True
    )

# ==============================================================================
# 9. KONTEN HALAMAN: FORM INPUT DATA BARU
# ==============================================================================
elif page_active == "Input":
    st.markdown("<h3 style='color: #1E293B; font-weight: 700;'>📝 Formulir Input Siswa Baru</h3>", unsafe_allow_html=True)
    st.write("Silakan isi form di bawah ini untuk menambahkan arsip buku induk baru:")
    
    with st.form("form_siswa_baru", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            in_nisn = st.text_input("Nomor NISN (10 Digit):")
            in_nis = st.text_input("Nomor NIS (Lokal):")
            in_nama = st.text_input("Nama Lengkap Siswa (Huruf Kapital):")
            in_jk = st.selectbox("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
        with c2:
            in_kelas = st.text_input("Rombel / Kelas Sekarang (Contoh: 3A):")
            in_tahun = st.selectbox("Tahun Masuk Angkatan:", ["2026", "2025", "2024", "2023", "2022", "2021"])
            in_tempat = st.text_input("Tempat Lahir:")
            in_alamat = st.text_area("Alamat Tinggal Lengkap:")
            
        tombol_simpan = st.form_submit_button("💾 Simpan Data ke Buku Induk")
        
        if tombol_simpan:
            if in_nisn and in_nis and in_nama:
                # Tentukan huruf pertama nama untuk abjad klapper otomatis
                huruf_depan = in_nama[0].upper() if len(in_nama) > 0 else "A"
                
                row_baru = pd.DataFrame([{
                    "NISN": in_nisn, "NIS": in_nis, "Nama Lengkap": in_nama.upper(),
                    "JK": in_jk, "Kelas": in_kelas, "Tahun Masuk": in_tahun,
                    "Abjad Klapper": huruf_depan, "Status": "Aktif",
                    "Tempat Lahir": in_tempat, "Tanggal Lahir": "2015-01-01", "Alamat": in_alamat
                }])
                
                st.session_state.siswa_db = pd.concat([st.session_state.siswa_db, row_baru], ignore_index=True)
                st.success(f"Berhasil! Data siswa bernama {in_nama.upper()} sudah disimpan ke database.")
            else:
                st.error("Gagal menyimpan, mohon isi field wajib (NISN, NIS, dan Nama Lengkap) terlebih dahulu!")

# ==============================================================================
# 10. ARSIP FOOTER BAWAH (Sesuai Standar PUSDIK)
# ==============================================================================
st.markdown("<br><br><br><hr style='border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)
col_foot1, col_foot2 = st.columns(2)
with col_foot1:
    st.markdown("<p style='color:#94A3B8; font-size:12px; font-family:sans-serif;'>PUSDIK 201.11</p>", unsafe_allow_html=True)
with col_foot2:
    st.markdown("<p style='color:#94A3B8; font-size:12px; font-family:sans-serif; text-align:right;'>© 2022 ANZFAAM FOUNDATION</p>", unsafe_allow_html=True)
