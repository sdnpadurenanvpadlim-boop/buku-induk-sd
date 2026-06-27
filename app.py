import streamlit as st
import pandas as pd
import base64

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(page_title="PUSDIK - Dashboard SDN Padurenan V", layout="wide", initial_sidebar_state="expanded")

# 2. DATA LOGO SEKOLAH (Base64 dari Logo SD Negeri Padurenan V)
LOGO_BASE64 = """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 t4FdOnQDpxXp9PgVOh/rfBXofFf9vwXwnpnxXrx T ArXpn9XwEnUfBPp6vgnp+K+Aen4fD6fInuFelf1 vAnqgOnq+rwTqZ0B6dP9vwXqnhmAnqGOn6+AnV8A OnArwAnToD04fVwPTAr6f7wT0vArU/FervT9YAnV PV4fDMCegPrUPrwInonoBPr8AenAr6V7oOnpxWun EfqYAnpjAr6vDPgPTMD1fDPu/wBwAngvTpw6AnU n7xAnonoBPpXqAOnAevEfqeBPrfAnpnwFfDPuAn pxHpx/6vAnTp4BPpXp0E6g/p/bCr+H0OAp04YFT pxPr8C/U+gE6dP9PivUnx6eK/rfEepXw8BPQHV 4dfV8Enw9fgU8dfHPpx4CenArXAr6Z8D0fEepX9 bAnpnhmBnpU+vwK9PHp+vwX1TArwT0B6nPAr0B6 Z/T4FfAnpXpjPgnpvxXqCenAenArxP6fwAng+v4E 9PA+pwAngZOnwK6U+L+vwPT8GvDPu/vBOvgE+r/ tfAr0PivXp0Hqn/W8CenTAJOnwAngZ6f7vU/X/Z B6ceAngUnUeBeno4FTqVfwEnpwHqxWvX8Z08V6U 4Ano3+ul6dfAvpn0AnonoBPivX8F6dOgAnpnvAn vAnqZ9P/W8FOnpXvKAnwPrgRPh6/ADXArpnoAng EnT9fCPr4AnXpnvAn+r06dfAr04fDPv8Au8Anw9 fh4Z4dfDInw9AnSvhjAnwK+tMeBXqnpAn0+HwfX 4FOnw+AnUn9fwJ+HivUnxGff4dfXArXAr06dfFf +NOnTPivXqVfAr0xU9fh/X6vhjXonqBPpwHqnAr 4GdEfX4AnpUvAnwAnT4dfvE9On/AFvAnpx4E6U/ FelfAnwHpxPh8BPTrXwK8CPr8EdfgOnEfqeBPrf ArpnwAnpHAr6/ivArwp4Z8V8V6en62BT0b4DOn4 FfwAnToZ/WwAnTpwA6V+D0fEToB6mQPVP+vwS enfAnVfAenX/p+A9MevgnTMDOnX/t4DpxHpx/6vAn U/XArXofVPVPVAnX4E9OfvE9M8PAnpxXrfHMCfX pnvKnj4D0/6eBXArpUvAnpxP1vgPTpwHpx4AnTr XwPT4dfEToVPRvxKeDPAnqjPAr0T4EevwHqfivU 4Anpn0AnToB6h8AnVPh0CdfvE9K+AnpxWuhPTMD On4Z8M+7+8AngE+Hw+vw AngE+ngE/6vwV6VAn Unw9PrArXpUvAnwHpxPh8BPTrXwK8CPr8F6lPx KeDPBPTAr6eGOnD0AnqGOnAepnwTpwPTpwPpwH6 v93wF9UeH+v3fBPQPTpxXpXpnqB6dP9vwK9T4BO vpX Ar6V6AnpnwAnXwAnpnoE69PDwE6dP+v3eUToAng OnFerv8AtfkPVPVAnV4dDPgVPAnpXwH18M/AnpH iE9PDG9M+vwA6f7pPTPVAnUnArunqfFPVPQPRPx KeCemegE6dP9vwX1X0A6fD6PBPp4fDPu/vAnpvq 8AnV8AOnArwD069BPTMDOnX/ALeAnXArwAngvpT wv0L6vAvUr+PgFOnTo+K9Sv8AW8D0/DPpT Ar4Z9 OfAnTp+vwU9On/AGwE+vr8OnDPuAnXwHqnhmBfW nj0AnonoAOn/T8vUPdfBfX/Z8CuvVPr8E+mAnX pnWvArXofXqOnRPgE9UdfwPT3vAnwPTpwA6ceA vVPh/u+KPr8CeHwAngvpnoB0+HgE+uE+vwPT8Z0 TAr4dfgI6fD+vgk9PDMCfD9eAvU4df93p+vwA9G PFPVPwPT8dfuE+An0+HwAngvpUnwf9XArunqfgT 1PDMCfXMDPH/W8pU9Y8AnrfW+AnU/AnrxPh8Ev Tpn ArXAr04n1fBPgJ1PwSdfvBOvAr6+Gfq+BXrUp+ K9SpXAn+vgU6dEwOmdE/H6vDOnRPV8AOnHArwB6 Z+sCfEdfDMDp/u/D0/vAnoxTr+vwCdfunwHpxKe FOgA6cPqYUnqHAngvpT7xgOnw+vAnU/reBXwp4 dfgOn636/gUnX/p/uFTon6vAjp9fAr06AnwPpw FTpx4FfGn6PwS6dP+vwE6dOnSvh0PVPgPUnAr4E 9PA+rwpwnpnvAenzPrwK8Cun4dfXw PT8M+Av0B6Z8AenwX9XgPT4FdPD/eK9OfAnXofVP VArw PTpwKeKfqvgJ0R/XAnqZAngfU+K6dfgZ0qfArwp +v ArqZAnXpwH6n6uBnpT/rfwUnpXwHq+uAnV8fAnp nvArXAr0qX8E9M9QPTA9X6uHpxAnXpnvAnwM9fA dPDyCefV8M+CdfunwPTg PTw AngvpxKeCelfArwHpj0/BPT8E+rgU+vgOn62AnUn Ar1PDwPT8dfuwK9CenArwp8PgE9Ovy8vVPVAnX MDPH/W8pU+HgE6dfAvpnvf7pU6Z8A+CegE9 PD/dE9E68BPTPXAnp16Z8CnDoE9MeBOnD0/28Anr fX4CddKfFfif8AGdOn/T/cFT4D1f6vgE69PDyP TPg PTpwPpnwE68D9XAr0AnsX9Hgvp6f7wK+OnToOn ED/AIeK9Sv4Ffff/Z8E6mBPRPvwUnwKeFOgHTp 94A9H++vUPHArU9PDw Ang/V4FdE/7vL0/VwPT8M9fArwK6ceBXwD6dfgnT4f7 3lGvTPg PTpxAnpw6dfuAnU4AngPTMDOnT/b/eD0PTMDp+t n Arwn9b5U/rfAr0T4DOnDp8vXw PT9bAp0+AnTpwE6nArUAnpnvAnp+rwT1PDwK8C enfArXAr0M9DPAr4GdPxnToPUnvAnphXp+vwCem AnUfAnwK9Gff8CnUfqvArrXp4FdPqgVOh8An1+ GdAenBOnDp0r6ZAnTp+vw PTpwFTqOvwAenAegD1enwPTA9XMD1DAr1BAnpxKe GfFfifUnwHpx8Anpw6cf+vA/TqE6dOBU+gAngA nXMDOnD6mAnR/V4dfwXpj/AEeBXwPpx/636vh nTr 0K+NOCfEfj4FfGvVp4+AnTp+K9Sn+vhjXpnoE9 EnUfBPphf7vT/teBPpnvAnp16CdSnBPT/AKXwT 6fivU/q+BXpj7xPh4BdenX7vkE6A6frYAnTr0 /V6/AnW/wB3wPT8M95eoPT8AnptTMD1fV4fAnp nh mBPS9D/tfKnj+r4KdP1v7pU9AnpHArXon6vDAnw K9PDAr4GdPAr4A9OnTAp6pAnUpxCenw AngEnU/XArpnAr4dfV4E9PDxM/ivpx/vD0/wBvw T6uAnphfgPTqPgE8F6dOgHTrXwA9OnDMDpxPr8 C dfwz7v7wPTMDpUAnVPT5enUPDPq/r+CenivgnX MD PH8AnUn4+Kdaf0uCnTpnxUnpXwAngvpXoPT8fA q deA+HAn0/FepnQD0B1ZAnU564CenX7wPTA+vCen AnpnwHpnwPTofAr0PivXp0Anpx/7XwS6VPgOnAn w PTgPTpw6/9vwAngHpxAnT7univBOnD0/wBvBX p iE9Anpx6fiv0vBOn4 df9rwPTgU9P/ALfBPpj8vVPVAnwPT MD1fDPu/wBwAngvTpw6AnU n7xAnonoBPpXqAOnAevEfqeBPrfArpnwAnpHAr 6/ivArwp4dfwPpwFT0/Fepfx+BX9MeAnWp9YF9On AnpwT0AnpnhgZ06f7vgJ1MAn+vgvpXpXunrYFT ArpXpn4AemPgfTAr4GdPAr6nArwAng/rfCPr+C PTp8M70PTMDpUAnpnvAnU+PgV9UevgPVP/AG+R 6e Ang+qfFep+gOnpX Ar4B9afh/vAnpHAnofivp6eBPpgfTA p6PArwp06A+rwUnonh4ZFTMDPHw+vw PTpxAnV8A OnAr4E+PAr6dPAr4E+PwInTp8uunArXp4dfgP h Th0TAr4dfgnTr8ugp1P1sCunHAr1PDAr6Y8M99 On Ar4dfgnpX9Xh4FfwCeD9fAvTrU

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
