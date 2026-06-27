import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(page_title="PUSDIK - Dashboard", layout="wide", initial_sidebar_state="expanded")

# 2. GAYA CSS PREMIUM (Agar warna, font, dan layout mirip 99% dengan gambar)
st.markdown("""
    <style>
    /* Mengatur warna latar belakang aplikasi menjadi abu-abu terang */
    .stApp {
        background-color: #F7FAFC;
    }
    /* Mengatur warna sidebar menjadi gelap sesuai gambar */
    [data-testid="stSidebar"] {
        background-color: #1A1D29 !important;
    }
    /* Sembunyikan elemen bawaan Streamlit yang mengganggu */
    header, footer {visibility: hidden;}
    
    /* Gaya Teks Menu Sidebar */
    .sidebar-category {
        color: #718096 !important;
        font-size: 11px !important;
        font-weight: bold !important;
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOPBAR / HEADER (Logout & User Profile)
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: white; padding: 10px 20px; border-bottom: 1px solid #E2E8F0; margin-top: -50px; margin-bottom: 20px;">
        <div>
            <button style="background-color: #FFF5F5; color: #E53E3E; border: 1px solid #FED7D7; padding: 6px 16px; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 14px;">
                <span style="margin-right: 5px;">🔄</span> Logout
            </button>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; font-family: sans-serif; color: #4A5568; font-size: 14px;">
            <span>Hi,</span>
            <div style="background-color: #E2W8F0; width: 32px; height: 32px; border-radius: 5px; background-color: #C6F6D5; color: #22543D; display: flex; align-items: center; justify-content: center; font-weight: bold;">
                A
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. DATABASE SEMENTARA (SESSION STATE)
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame([
        {"nisn": "3034930290", "nis": "2025352", "nama_lengkap": "WIIWJFKJW", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "SDDMNNBVSDMV", "nama_ayah": "WEVWV", "nama_ibu": "QWCFWEQ", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930291", "nis": "2025353", "nama_lengkap": "Budi Santoso", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Jl. Merdeka", "nama_ayah": "Slamet", "nama_ibu": "Siti", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930292", "nis": "2025354", "nama_lengkap": "Siti Aminah", "jenis_kelamin": "Perempuan", "alamat_lengkap": "Jl. Mawar", "nama_ayah": "Rahmat", "nama_ibu": "Ani", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930293", "nis": "2019355", "nama_lengkap": "Andi Wijaya", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Jl. Melati", "nama_ayah": "Tono", "nama_ibu": "Ika", "kelas_sekarang": "Lulus", "tahun_masuk": "2019", "status": "Lulus"}
    ])

# 5. SIDEBAR DENGAN STRUKTUR PERSIS GAMBAR
with st.sidebar:
    st.markdown("<h2 style='color: white; font-family: sans-serif; letter-spacing: 3px; margin-bottom: 30px;'>PUSDIK</h2>", unsafe_allow_html=True)
    
    # Navigasi Utama menggunakan Selectbox yang disamarkan
    st.markdown("<p class='sidebar-category'>DASHBOARD</p>", unsafe_allow_html=True)
    buka_dashboard = st.checkbox("🔷 Dashboard Utama", value=True)
    
    st.markdown("<p class='sidebar-category'>MAIN MENU</p>", unsafe_allow_html=True)
    menu_main = st.selectbox("", [" Pilih Menu Data Utama...", "📝 Data Utama (>)", "📊 Data Kelas (>)"], label_visibility="collapsed")
    
    st.markdown("<p class='sidebar-category'>PENILAIAN</p>", unsafe_allow_html=True)
    menu_nilai = st.selectbox("", [" Pilih Menu Penilaian...", "📶 Basic Data Setting (>)", "📝 Input Penilaian (>)"], label_visibility="collapsed")
    
    st.markdown("<p class='sidebar-category'>DOKUMEN DAN BUKU INDUK</p>", unsafe_allow_html=True)
    menu_dokumen = st.selectbox("", [" Pilih Menu Dokumen...", "📖 Dokumen Siswa (>)", "📋 Lihat & Cetak Buku Induk (>)"], label_visibility="collapsed")

# Logika Penentu Menu Aktif
pilihan = "Dashboard"
if "Data Utama" in menu_main: pilihan = "Input"
elif "Data Kelas" in menu_main: pilihan = "Import"
elif "Cetak Buku Induk" in menu_dokumen: pilihan = "Cetak"

# 6. KONTEN HALAMAN UTAMA
if pilihan == "Dashboard":
    st.markdown("<h3 style='color: #4A5568; font-family: sans-serif; font-weight: bold; margin-bottom: 20px;'>DASHBOARD</h3>", unsafe_allow_html=True)
    
    # BAGIAN UTAMA: Kiri (Grafik Batang) & Kanan (Kartu Dashboard)
    kolom_kiri, kolom_kanan = st.columns([6, 5])
    
    with kolom_kiri:
        # Kotak Putih Latar Belakang Grafik
        st.markdown("""
            <div style="background-color: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #E2E8F0; min-height: 420px;">
                <p style="color: #4A5568; font-weight: bold; font-size: 15px; margin-bottom: 25px;">📊 JML Pesdik MTS 10th Terakhir Per Thn Masuk</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Grafik Batang Berwarna (Ungu dan Oranye ditaruh tepat di atas kotak menggunakan trik layout)
        df_chart = st.session_state.data.groupby(['tahun_masuk', 'jenis_kelamin']).size().unstack(fill_value=0)
        if not df_chart.empty:
            # Warna chart otomatis mengikuti palet tema Streamlit yang cerah mendekati gambar
            st.bar_chart(df_chart, height=320)
            
    with kolom_kanan:
        # --- BARIS ATAS: KARTU GURU (Ungu dan Merah Besar) ---
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
                <div style="background-color: #9061F9; padding: 25px; border-radius: 15px; color: white; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <div style="font-size: 36px; font-weight: bold; margin-bottom: 5px;">7</div>
                    <div style="font-size: 14px; font-weight: 500; opacity: 0.95;">Guru Aktif</div>
                    <span style="position: absolute; right: 20px; top: 25px; font-size: 30px; opacity: 0.3;">👤+</span>
                </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown("""
                <div style="background-color: #F05252; padding: 25px; border-radius: 15px; color: white; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <div style="font-size: 36px; font-weight: bold; margin-bottom: 5px;">1</div>
                    <div style="font-size: 14px; font-weight: 500; opacity: 0.95;">Guru Non Aktif</div>
                    <span style="position: absolute; right: 20px; top: 25px; font-size: 30px; opacity: 0.3;">👤+</span>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        
        # --- BARIS BAWAH: KARTU STATUS SISWA (4 Kotak Kecil Berwarna Sesuai Gambar) ---
        df_siswa = st.session_state.data
        aktif = len(df_siswa[df_siswa['status'] == 'Aktif'])
        lulus = len(df_siswa[df_siswa['status'] == 'Lulus'])
        pindah = len(df_siswa[df_siswa['status'] == 'Pindah'])
        non_akt = len(df_siswa[df_siswa['status'] == 'Non Aktif'])
        
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.markdown(f"""
                <div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <div style="color: #7C3AED; font-size: 24px; font-weight: bold;">{aktif}</div>
                    <div style="color: #94A3B8; font-size: 11px; font-weight: bold; margin-top: 5px;">Aktif</div>
                </div>
            """, unsafe_allow_html=True)
        with col_s2:
            st.markdown(f"""
                <div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <div style="color: #0D9488; font-size: 24px; font-weight: bold;">{lulus}</div>
                    <div style="color: #94A3B8; font-size: 11px; font-weight: bold; margin-top: 5px;">Lulus</div>
                </div>
            """, unsafe_allow_html=True)
        with col_s3:
            st.markdown(f"""
                <div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <div style="color: #D97706; font-size: 24px; font-weight: bold;">{pindah}</div>
                    <div style="color: #94A3B8; font-size: 11px; font-weight: bold; margin-top: 5px;">Pindah</div>
                </div>
            """, unsafe_allow_html=True)
        with col_s4:
            st.markdown(f"""
                <div style="background-color: white; padding: 15px 10px; border-radius: 12px; text-align: center; border: 1px solid #E2E8F0; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <div style="color: #E11D48; font-size: 24px; font-weight: bold;">{non_akt}</div>
                    <div style="color: #94A3B8; font-size: 11px; font-weight: bold; margin-top: 5px;">Non Aktif</div>
                </div>
            """, unsafe_allow_html=True)

# 7. FITUR INPUT DATA (MAIN MENU 1)
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
        tahun_masuk = st.selectbox("TAHUN MASUK:", ["2026", "2025", "2024", "2023", "2022", "2021", "2020", "2019"])
        status = st.selectbox("STATUS SISWA:", ["Aktif", "Lulus", "Pindah", "Non Aktif"])
        
        if st.form_submit_button("Simpan"):
            new_data = pd.DataFrame([{"nisn": nisn, "nis": nis, "nama_lengkap": nama_lengkap, "jenis_kelamin": jenis_kelamin, "alamat_lengkap": alamat_lengkap, "nama_ayah": nama_ayah, "nama_ibu": nama_ibu, "kelas_sekarang": kelas_sekarang, "tahun_masuk": tahun_masuk, "status": status}])
            st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
            st.success("Data Berhasil Disimpan!")

# 8. FITUR IMPORT EXCEL (MAIN MENU 2)
elif pilihan == "Import":
    st.subheader("📥 Import Data Kelas via Excel")
    uploaded_file = st.file_uploader("Upload File Excel", type=["xlsx"])
    if uploaded_file:
        df_excel = pd.read_excel(uploaded_file)
        df_excel.columns = df_excel.columns.str.strip().str.lower().str.replace(" ", "_")
        st.session_state.data = pd.concat([st.session_state.data, df_excel], ignore_index=True)
        st.success("Sukses Import!")

# 9. FITUR LIHAT & CETAK BUKU INDUK LENGKAP
elif pilihan == "Cetak":
    st.subheader("🗂️ Cetak Data Buku Induk Lengkap")
    df_tampil = st.session_state.data.copy()
    kolom_wajib = ["nisn", "nis", "nama_lengkap", "jenis_kelamin", "alamat_lengkap", "nama_ayah", "nama_ibu", "kelas_sekarang"]
    df_tampil = df_tampil[[c for c in kolom_wajib if c in df_tampil.columns]]
    df_tampil = df_tampil.rename(columns={"nisn":"NISN","nis":"NIS","nama_lengkap":"NAMA LENGKAP","jenis_kelamin":"JK","alamat_lengkap":"ALAMAT","nama_ayah":"AYAH","nama_ibu":"IBU","kelas_sekarang":"KELAS"})
    
    st.dataframe(df_tampil, use_container_width=True)
    
    html_table = df_tampil.to_html(index=False)
    html_print = f"<html><head><style>body{{font-family:sans-serif;padding:20px;}}table{{width:100%;border-collapse:collapse;}}th,td{{border:1px solid black;padding:8px;}}th{{background-color:#f2f2f2;}}</style></head><body><h2>DATA BUKU INDUK</h2>{html_table}<script>window.onload=function(){{window.print();}}</script></body></html>"
    st.download_button(label="🖨️ Download File Siap Cetak (HTML)", data=html_print, file_name="buku_induk.html", mime="text/html")

# 10. FOOTER BAWAH PERSIS GAMBAR
st.markdown("<br><br><br>", unsafe_allow_html=True)
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("<p style='color:#A0AEC0; font-size:12px; font-family:sans-serif;'>PUSDIK 201.11</p>", unsafe_allow_html=True)
with col_f2:
    st.markdown("<p style='color:#A0AEC0; font-size:12px; font-family:sans-serif; text-align:right;'>© 2022 ANZFAAM FOUNDATION</p>", unsafe_allow_html=True)
