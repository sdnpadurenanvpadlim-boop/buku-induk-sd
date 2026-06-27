import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# KONEKSI DATABASE AUTOMATIS
conn = sqlite3.connect('buku_induk_sd.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS buku_induk (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nis TEXT UNIQUE,
        nisn TEXT,
        nama_lengkap TEXT,
        nama_panggilan TEXT,
        jenis_kelamin TEXT,
        tempat_lahir TEXT,
        tanggal_lahir TEXT,
        agama TEXT,
        alamat TEXT,
        kelas_sekarang TEXT,
        nama_ayah TEXT,
        nama_ibu TEXT,
        pekerjaan_ortu TEXT,
        status_siswa TEXT DEFAULT 'Aktif'
    )
''')
conn.commit()

st.set_page_config(page_title="Buku Induk & Klapper SD", layout="wide", page_icon="📚")

st.markdown("""
    <div style="background-color:#1E3A8A;padding:20px;border-radius:10px;margin-bottom:25px">
    <h1 style="color:white;text-align:center;margin:0;">BUKU INDUK & KLAPPER DIGITAL SD</h1>
    <p style="color:#E2E8F0;text-align:center;margin:5px 0 0 0;">Aplikasi Administrasi Sekolah Dasar</p>
    </div>
""", unsafe_allow_html=True)

# TAMBAHAN MENU IMPOR EXCEL DI SINI
menu = ["📊 Dashboard", "📝 Input Buku Induk", "🔍 Lihat & Cetak", "🗂️ Buku Klapper (A-Z)", "📥 Import Excel"]
choice = st.sidebar.selectbox("MENU", menu)

if choice == "📊 Dashboard":
    st.subheader("Statistik Siswa")
    df = pd.read_sql_query("SELECT * FROM buku_induk", conn)
    if not df.empty:
        col1, col2 = st.columns(2)
        col1.metric("Total Siswa", len(df))
        col2.metric("Siswa Aktif", len(df[df['status_siswa'] == 'Aktif']))
    else:
        st.info("Belum ada data. Silakan isi di menu Input Buku Induk atau Import Excel.")

elif choice == "📝 Input Buku Induk":
    st.subheader("Formulir Buku Induk Baru")
    with st.form("form_siswa"):
        nis = st.text_input("NIS (Wajib)")
        nama = st.text_input("Nama Lengkap (Wajib)")
        jk = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        kelas = st.selectbox("Kelas", ["1", "2", "3", "4", "5", "6"])
        ayah = st.text_input("Nama Ayah")
        ibu = st.text_input("Nama Ibu")
        submitted = st.form_submit_button("Simpan Data")
        if submitted:
            if nis and nama:
                try:
                    c.execute("INSERT INTO buku_induk (nis, nama_lengkap, jenis_kelamin, kelas_sekarang, nama_ayah, nama_ibu) VALUES (?,?,?,?,?,?)", (nis, nama, jk, kelas, ayah, ibu))
                    conn.commit()
                    st.success("Data berhasil disimpan!")
                except:
                    st.error("NIS sudah terdaftar!")
            else:
                st.warning("NIS dan Nama harus diisi!")

elif choice == "🔍 Lihat & Cetak":
    st.subheader("Data Buku Induk")
    df = pd.read_sql_query("SELECT nis, nama_lengkap, jenis_kelamin, kelas_sekarang FROM buku_induk", conn)
    st.dataframe(df, use_container_width=True)

elif choice == "🗂️ Buku Klapper (A-Z)":
    st.subheader("Buku Klapper (Urutan Abjad)")
    df_klapper = pd.read_sql_query("SELECT nama_lengkap, nis, kelas_sekarang FROM buku_induk ORDER BY nama_lengkap ASC", conn)
    if not df_klapper.empty:
        st.table(df_klapper)
    else:
        st.info("Data masih kosong.")

# --- FITUR KODE BARU: MENU IMPORT EXCEL ---
elif choice == "📥 Import Excel":
    st.subheader("Unggah Data Siswa Sekaligus dari Excel")
    st.write("Pastikan file Excel Anda memiliki kolom dengan judul persis: **nis**, **nama**, **jk**, **kelas**, **ayah**, **ibu**")
    
    file_excel = st.file_uploader("Pilih File Excel (.xlsx)", type=["xlsx"])
    
    if file_excel is not None:
        try:
            df_upload = pd.read_excel(file_excel)
            st.write("Pratinjau data Excel yang dibaca:")
            st.dataframe(df_upload.head())
            
            tombol_proses = st.button("Masukkan Semua Data ke Aplikasi")
            
            if tombol_proses:
                sukses = 0
                gagal = 0
                for index, baris in df_upload.iterrows():
                    try:
                        c.execute("""
                            INSERT INTO buku_induk (nis, nama_lengkap, jenis_kelamin, kelas_sekarang, nama_ayah, nama_ibu) 
                            VALUES (?,?,?,?,?,?)
                        """, (str(baris['nis']), str(baris['nama']), str(baris['jk']), str(baris['kelas']), str(baris['ayah']), str(baris['ibu'])))
                        sukses += 1
                    except:
                        gagal += 1
                conn.commit()
                st.success(f"Proses Selesai! {sukses} data siswa berhasil diimport. Gagal (atau NIS sudah ada): {gagal}")
        except Exception as e:
            st.error(f"Eror saat membaca file: {e}")
            # Tambahkan tombol ini di bawah tabel/dataframe Kakak
    st.markdown("---")
    st.subheader("🖨️ Cetak Dokumen")
    st.write("Klik tombol di bawah ini untuk mencetak halaman atau menyimpannya sebagai file PDF:")
    
    # Tombol pemicu cetak browser
    st.button("Print / Simpan Ke PDF", on_click=st.js_on_response("window.print()"))
