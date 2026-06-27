elif menu == "🔍 Lihat & Cetak":
    st.subheader("🗂️ Cetak Data Buku Induk Lengkap")
    
    # CSS Khusus agar saat dicetak (Ctrl+P / Tombol Print), tampilan rapi & sidebar otomatis hilang
    st.markdown("""
        <style>
        @media print {
            /* Sembunyikan sidebar, tombol, dan elemen Streamlit lainnya */
            [data-testid="stSidebar"], button, header, .stDeployButton, [data-testid="stToolbar"] {
                display: none !important;
            }
            /* Lebarkan konten utama agar pas di kertas */
            .main .block-container {
                padding: 0 !important;
                max-width: 100% !important;
            }
            /* Desain tabel khusus cetak agar garisnya jelas */
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

    # Memuat data (Pastikan st.session_state.data sesuai dengan variabel penyimpanan Kakak)
    if "data" in st.session_state and not st.session_state.data.empty:
        df_tampil = st.session_state.data.copy()
        
        # Kolom yang diwajibkan oleh Kakak
        kolom_lengkap = ["nisn", "nis", "nama_lengkap", "jenis_kelamin", "alamat_lengkap", "nama_ayah", "nama_ibu", "kelas_sekarang"]
        
        # Filter kolom yang ada di data saja agar tidak eror jika ada yang belum terisi
        kolom_ada = [col for col in kolom_lengkap if col in df_tampil.columns]
        
        df_tampil = df_tampil[kolom_ada]
        
        # Mengubah nama kolom agar rapi saat dilihat & dicetak
        nama_kolom_baru = {
            "nisn": "NISN",
            "nis": "NIS",
            "nama_lengkap": "NAMA LENGKAP",
            "jenis_kelamin": "JK",
            "alamat_lengkap": "ALAMAT LENGKAP",
            "nama_ayah": "NAMA AYAH",
            "nama_ibu": "NAMA IBU",
            "kelas_sekarang": "KELAS"
        }
        df_tampil = df_tampil.rename(columns=nama_kolom_baru)
        
        # Menampilkan dalam bentuk tabel HTML asli agar bisa dicetak dengan rapi oleh browser
        st.write("### DATA SISWA BUKU INDUK")
        st.markdown(df_tampil.to_html(index=False, escape=False), unsafe_allow_html=True)
        
        # Tombol Cetak Pintar
        st.markdown("---")
        st.subheader("🖨️ Tindakan")
        st.markdown('<button onclick="window.print()" style="padding: 12px 24px; background-color: #1E3A8A; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 16px;">🖨️ Cetak / Simpan ke PDF</button>', unsafe_allow_html=True)
        
    else:
        st.info("Belum ada data Buku Induk yang tersimpan. Silakan input data terlebih dahulu atau import file Excel.")
