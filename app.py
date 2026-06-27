import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(page_title="PUSDIK - Buku Induk Digital", layout="wide")

# 2. HEADER ATAS (Mirip Topbar di Gambar)
col_logo, col_logout, col_user = st.columns([2, 8, 2])
with col_logo:
    st.markdown("<h2 style='margin:0; color:#1E3A8A; font-family:sans-serif; letter-spacing: 2px;'>PUSDIK</h2>", unsafe_allow_html=True)
with col_logout:
    st.markdown("<button style='background-color:#FFF5F5; color:#E53E3E; border:1px solid #FED7D7; padding:5px 15px; border-radius:5px; font-weight:bold; cursor:pointer;'>🛑 Logout</button>", unsafe_allow_html=True)
with col_user:
    st.markdown("<div style='text-align:right; font-weight:bold; color:#4A5568;'>Hi, <span style='background-color:#E2E8F0; padding:5px 10px; border-radius:5px; color:#2B6CB0;'>A</span></div>", unsafe_allow_html=True)

st.markdown("---")

# 3. DATABASE SEMENTARA (SESSION STATE)
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame([
        # Data contoh awal agar dashboard tidak kosong saat pertama dibuka
        {"nisn": "3034930290", "nis": "2025352", "nama_lengkap": "WIIWJFKJW", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "SDDMNNBVSDMV", "nama_ayah": "WEVWV", "nama_ibu": "QWCFWEQ", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930291", "nis": "2025353", "nama_lengkap": "Budi Santoso", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Jl. Merdeka No. 1", "nama_ayah": "Slamet", "nama_ibu": "Siti", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930292", "nis": "2025354", "nama_lengkap": "Siti Aminah", "jenis_kelamin": "Perempuan", "alamat_lengkap": "Jl. Mawar No. 12", "nama_ayah": "Rahmat", "nama_ibu": "Ani", "kelas_sekarang": "3A", "tahun_masuk": "2020", "status": "Aktif"},
        {"nisn": "3034930293", "nis": "2019355", "nama_lengkap": "Andi Wijaya", "jenis_kelamin": "Laki-laki", "alamat_lengkap": "Jl. Melati No. 5", "nama_ayah": "Tono", "nama_ibu": "Ika", "kelas_sekarang": "Lulus", "tahun_masuk": "2019", "status": "Lulus"}
    ])

# 4. SIDEBAR MENU BERKELOMPOK (Sesuai Struktur di Gambar)
st.sidebar.markdown("### 📊 DASHBOARD")
menu_dashboard = st.sidebar.checkbox("Dashboard Utama", value=True)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color:#A0AEC0; font-size:12px; font-weight:bold; margin-bottom:5px;'>MAIN MENU</p>", unsafe_allow_html=True)
menu_main = st.sidebar.selectbox("Pilih Menu Data:", ["-", "📝 Input Buku Induk", "📥 Import Excel", "🔍 Lihat & Cetak"])

st.sidebar.markdown("<p style='color:#A0AEC0; font-size:12px; font-weight:bold; margin-bottom:5px;'>DOKUMEN DAN BUKU INDUK</p>", unsafe_allow_html=True)
menu_dokumen = st.sidebar.selectbox("Pilih Instrumen:", ["-", "📁 Dokumen Siswa", "📋 Instrumen"])

# Penentu Menu Aktif
if menu_main != "-":
    pilihan_menu = menu_main
elif menu_dokumen != "-":
    pilihan_menu = menu_dokumen
else:
    pilihan_menu = "Dashboard Utama"

# 5. HALAMAN KONTEN UTAMA
if pilihan_menu == "Dashboard Utama":
    st.markdown("<h2 style='margin-top:0;'>DASHBOARD UTAMA</h2>", unsafe_allow_html=True)
    
    # MEMBUAT DUA KOLOM BESAR (Kiri: Grafik, Kanan: Kartu Metrik)
    kolom_kiri, kolom_kanan = st.columns([6, 5])
    
    with kolom_kiri:
        st.markdown("<div style='background-color:white; padding:15px; border-radius:10px; border:1px solid #E2E8F0;'>", unsafe_allow_html=True)
        st.subheader("📊 JML Pesdik MTS 10th Terakhir Per Thn Masuk")
        
        # Mengolah data siswa untuk dijadikan grafik batang per tahun masuk
        df_chart = st.session_state.data.groupby(['tahun_masuk', 'jenis_kelamin']).size().unstack(fill_value=0)
        if not df_chart.empty:
            st.bar_chart(df_chart)
        else:
            st.info("Belum ada data untuk grafik.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with kolom_kanan:
        # Baris Kartu Guru (Ungu dan Merah)
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
                <div style='background-color:#7C3AED; padding:20px; border-radius:15px; color:white; margin-bottom:15px;'>
                    <span style='font-size:24px; font-weight:bold;'>7</span><br>
                    <span style='font-size:14px; opacity:0.9;'>👤 Guru Aktif</span>
                </div>
            """, unsafe_allow_html=True)
        with col_g2:
            st.markdown("""
                <div style='background-color:#F87171; padding:20px; border-radius:15px; color:white; margin-bottom:15px;'>
                    <span style='font-size:24px; font-weight:bold;'>1</span><br>
                    <span style='font-size:14px; opacity:0.9;'>👤 Guru Non Aktif</span>
                </div>
            """, unsafe_allow_html=True)
            
        # Baris Kartu Status Siswa (Sesuai data nyata di session_state)
        df_siswa = st.session_state.data
        jml_aktif = len(df_siswa[df_siswa['status'] == 'Aktif'])
        jml_lulus = len(df_siswa[df_siswa['status'] == 'Lulus'])
        jml_pindah = len(df_siswa[df_siswa['status'] == 'Pindah'])
        jml_non_aktif = len(df_siswa[df_siswa['status'] == 'Non Aktif'])

        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.markdown(f"<div style='background-color:#EFF6FF; padding:15px; border-radius:10px; text-align:center; border:1px solid #BFDBFE;'><h3 style='color:#1E40AF; margin:0;'>{jml_aktif}</h3><p style='color:#1E40AF; font-size:12px; margin:0;'>Aktif</p></div>", unsafe_allow_html=True)
        with col_s2:
            st.markdown(f"<div style='background-color:#ECFDF5; padding:15px; border-radius:10px; text-align:center; border:1px solid #A7F3D0;'><h3 style='color:#065F46; margin:0;'>{jml_lulus}</h3><p style='color:#065F46; font-size:12px; margin:0;'>Lulus</p></div>", unsafe_allow_html=True)
        with col_s3:
            st.markdown(f"<div style='background-color:#FFFBEB; padding:15px; border-radius:10px; text-align:center; border:1px solid #FDE68A;'><h3 style='color:#92400E; margin:0;'>{jml_pindah}</h3><p style='color:#92400E; font-size:12px; margin:0;'>Pindah</p></div>", unsafe_allow_html=True)
        with col_s4:
            st.markdown(f"<div style='background-color:#FEF2F2; padding:15px; border-radius:10px; text-align:center; border:1px solid #FCA5A5;'><h3 style='color:#991B1B; margin:0;'>{jml_non_aktif}</h3><p style='color:#991B1B; font-size:12px; margin:0;'>Non Aktif</p></div>", unsafe_allow_html=True)

# 6. KODE MENU UTAMA LAINNYA (TETAP TERJAGA AMAN)
elif pilihan_menu == "📝 Input Buku Induk":
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
        tahun_masuk = st.selectbox("TAHUN MASUK:", ["2026", "2025", "2024", "2023", "2022", "2021", "2020", "2019"])
        status = st.selectbox("STATUS SISWA:", ["Aktif", "Lulus", "Pindah", "Non Aktif"])
        
        submitted = st.form_submit_button("Simpan Data")
        if submitted:
            new_data = pd.DataFrame([{
                "nisn": nisn, "nis": nis, "nama_lengkap": nama_lengkap, 
                "jenis_kelamin": jenis_kelamin, "alamat_lengkap": alamat_lengkap, 
                "nama_ayah": nama_ayah, "nama_ibu": nama_ibu, "kelas_sekarang": kelas_sekarang,
                "tahun_masuk": tahun_masuk, "status": status
            }])
            st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
            st.success("Data berhasil ditambahkan ke database!")

elif pilihan_menu == "📥 Import Excel":
    st.subheader("📥 Import Data dari Excel")
    uploaded_file = st.file_uploader("Pilih file Excel (.xlsx)", type=["xlsx"])
    if uploaded_file is not None:
        try:
            df_excel = pd.read_excel(uploaded_file)
            df_excel.columns = df_excel.columns.str.strip().str.lower().str.replace(" ", "_")
            st.session_state.data = pd.concat([st.session_state.data, df_excel], ignore_index=True)
            st.success("Data Excel berhasil digabungkan!")
            st.dataframe(df_excel)
        except Exception as e:
            st.error(f"Gagal memproses file Excel: {e}")

elif pilihan_menu == "🔍 Lihat & Cetak":
    st.subheader("🗂️ Cetak Data Buku Induk Lengkap")
    if not st.session_state.data.empty:
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
        st.dataframe(df_tampil, use_container_width=True)
        
        # Fitur Cetak Pintar via Download HTML (Cara aman Anti-Gagal kemarin)
        html_table = df_tampil.to_html(index=False)
        html_print = f"<html><head><style>body{{font-family:sans-serif;padding:20px;}}table{{width:100%;border-collapse:collapse;}}th,td{{border:1px solid black;padding:8px;text-align:left;}}th{{background-color:#f2f2f2;}}</style></head><body><h2>DATA SISWA BUKU INDUK</h2>{html_table}<script>window.onload=function(){{window.print();}}</script></body></html>"
        
        st.download_button(label="📥 Download File Siap Cetak (HTML)", data=html_print, file_name="buku_induk_cetak.html", mime="text/html")
    else:
        st.info("Database kosong.")

# 7. FOOTER HALAMAN (Sesuai Gambar)
st.markdown("<br><hr>", unsafe_allow_html=True)
col_foot1, col_foot2 = st.columns(2)
with col_foot1:
    st.markdown("<p style='color:#A0AEC0; font-size:12px;'>PUSDIK 201.11</p>", unsafe_allow_html=True)
with col_foot2:
    st.markdown("<p style='color:#A0AEC0; font-size:12px; text-align:right;'>© 2026 ANZFAM FOUNDATION</p>", unsafe_allow_html=True)
