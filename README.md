# Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python

## 1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python merupakan program untuk membaca data nilai siswa dari berkas teks, memvalidasi data, menghitung statistik dasar, menentukan ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), dan menyimpan hasil analisis ke dalam berkas laporan.

Proyek ini dikembangkan sebagai implementasi materi Algoritma dan Pemrograman, khususnya penggunaan fungsi, struktur data, validasi masukan, penanganan berkas, pengujian program, debugging, dan dokumentasi proyek.

## 2. Tujuan Program

Program ini bertujuan untuk:
1. Membaca data nama dan nilai siswa dari berkas teks.
2. Memvalidasi data agar hanya data yang memenuhi ketentuan yang digunakan.
3. Menghitung jumlah data valid, nilai rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status ketuntasan siswa berdasarkan KKM.
5. Menampilkan hasil analisis pada terminal.
6. Menyimpan laporan analisis ke dalam berkas teks.
7. Menguji fungsi program melalui beberapa skenario pengujian.

## 3. Fitur Utama

- Membaca data nilai siswa dari berkas `.txt`.
- Memeriksa format data dan rentang nilai.
- Mengabaikan data yang tidak memenuhi ketentuan.
- Menghitung statistik dasar nilai siswa.
- Menentukan status ketuntasan berdasarkan KKM 75.
- Menampilkan ringkasan hasil analisis.
- Menyimpan laporan ke dalam berkas teks.
- Menjalankan pengujian otomatis untuk memeriksa perilaku program.

## 4. Teknologi dan Persyaratan

- Bahasa pemrograman: Python.
- Editor kode: Visual Studio Code.
- Format data masukan: berkas teks `.txt`.
- Format laporan: berkas teks `.txt`.
- Pengujian otomatis: modul `unittest` dari Python.

Python perlu terpasang pada komputer agar program dapat dijalankan.

## 5. Struktur Proyek

```text
proyek-analisis-nilai-2225250071/
├── data/
│   ├── nilai_contoh.txt
│   ├── uji_tc01.txt
│   ├── uji_tc02.txt
│   ├── uji_tc03.txt
│   └── uji_tc08.txt
├── output/
│   ├── .gitkeep
│   └── laporan_analisis.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   └── scripts/
│       ├── uji_analisis.py
│       ├── uji_data_io.py
│       ├── uji_tc01.py
│       ├── uji_tc02.py
│       ├── uji_tc03.py
│       ├── uji_tc04.py
│       ├── uji_tc05.py
│       ├── uji_tc06.py
│       ├── uji_tc07.py
│       ├── uji_tc08.py
│       └── uji_utilitas.py
├── docs/
│   └── screenshot/
│       └── .gitkeep
├── proposal.md
├── README.md
└── .gitignore
```

Keterangan:
- `data/` menyimpan data contoh dan berkas masukan untuk beberapa skenario pengujian.
- `output/` digunakan untuk menyimpan laporan hasil analisis.
- `src/` berisi kode sumber program.
- `tests/` berisi dokumentasi skenario dan skrip pengujian.
- `docs/screenshot/` disiapkan untuk dokumentasi visual proyek.
- `proposal.md` berisi proposal proyek.
- `.gitignore` mengatur berkas yang tidak perlu dimasukkan ke repositori Git.

## 6. Format Data Masukan

Data utama disimpan dalam berkas `data/nilai_contoh.txt`. Setiap baris berisi nama siswa dan nilai yang dipisahkan oleh tanda koma.

Contoh:

```text
Alya,80
Bima,70
Citra,90
Dimas,75
Eka,60
Fajar,85
Gita,95
Hana,65
```

Ketentuan data:
- Nama siswa tidak boleh kosong.
- Nilai harus berupa angka.
- Nilai yang digunakan dalam analisis harus berada pada rentang 0 sampai 100.
- Baris kosong dan data dengan format yang tidak sesuai ditangani sesuai validasi program.
- KKM yang digunakan adalah 75.

## 7. Cara Menjalankan Program

Buka terminal di Visual Studio Code dan pastikan direktori aktif berada pada folder utama proyek.

Jalankan program menggunakan perintah berikut pada PowerShell:

```powershell
& "C:\Users\USER\.local\bin\python3.14.exe" -m src.main
```

Jika Python telah terdaftar pada PATH komputer, program juga dapat dijalankan menggunakan:

```powershell
python -m src.main
```

Program akan membaca data dari `data/nilai_contoh.txt`, menampilkan hasil analisis pada terminal, dan menyimpan laporan ke `output/laporan_analisis.txt`.

Catatan: perintah pertama menggunakan lokasi Python pada komputer pengembang. Jika proyek dijalankan di komputer lain, sesuaikan perintah tersebut dengan instalasi Python yang tersedia.

## 8. Hasil Program

Berdasarkan data contoh yang disediakan, program menghasilkan ringkasan berikut:

| Komponen | Hasil |
|---|---:|
| Jumlah data valid | 8 |
| Nilai rata-rata | 77,50 |
| Nilai tertinggi | 95 |
| Nilai terendah | 60 |
| KKM | 75 |
| Siswa tuntas | 5 |
| Siswa belum tuntas | 3 |

Laporan lengkap disimpan dalam berkas `output/laporan_analisis.txt`.

## 9. Pembagian Modul Program

- `src/main.py`: mengatur alur utama program dan memanggil fungsi-fungsi yang diperlukan.
- `src/data_io.py`: menangani pembacaan data siswa dan penyimpanan laporan.
- `src/analisis.py`: menangani validasi nilai, perhitungan statistik, dan penentuan ketuntasan.
- `src/utilitas.py`: membantu penyusunan laporan analisis.
- `tests/test_case.md`: mendokumentasikan skenario dan hasil pengujian.
- `tests/scripts/`: menyimpan skrip pengujian program.

## 10. Pengujian Program

Program telah menjalani delapan skenario pengujian otomatis menggunakan `unittest`. Pengujian mencakup kondisi berikut.

| No. | Skenario | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Data nilai normal | Statistik sesuai data yang valid | Sesuai hasil pengujian | LULUS |
| 2 | Nilai minimum 0 | Nilai 0 dapat diproses | Sesuai hasil pengujian | LULUS |
| 3 | Nilai maksimum 100 | Nilai 100 dapat diproses | Sesuai hasil pengujian | LULUS |
| 4 | Nilai di luar rentang | Nilai tidak valid ditangani sesuai ketentuan | Sesuai hasil pengujian | LULUS |
| 5 | Berkas tidak ditemukan | Program menangani kondisi berkas yang tidak tersedia | Sesuai hasil pengujian | LULUS |
| 6 | Semua siswa tuntas | Status ketuntasan dihitung dengan benar | Sesuai hasil pengujian | LULUS |
| 7 | Nilai di sekitar KKM | Status ketuntasan sesuai batas KKM | Sesuai hasil pengujian | LULUS |
| 8 | Tidak ada data valid | Program menangani kondisi tanpa data valid | Sesuai hasil pengujian | LULUS |

Pengujian otomatis dijalankan melalui perintah berikut:

```powershell
& "C:\Users\USER\.local\bin\python3.14.exe" -m unittest discover -s tests\scripts -p "uji_tc*.py" -v
```

Hasil pengujian terakhir menunjukkan delapan pengujian dijalankan dan seluruhnya lulus.

Dokumentasi skenario pengujian dapat dilihat pada `tests/test_case.md`.

## 11. Penanganan Kesalahan dan Pengembangan

Program dirancang untuk menangani masukan yang tidak sesuai dan kondisi berkas yang tidak ditemukan melalui mekanisme validasi dan penanganan kesalahan.

Pengembangan selanjutnya dapat mencakup penambahan antarmuka pengguna, fitur pencarian nama siswa, pengurutan nilai, serta ekspor laporan ke format lain.

## 12. Dokumentasi dan Referensi

Proyek ini dikembangkan sebagai implementasi materi Algoritma dan Pemrograman, khususnya fungsi, struktur data, pengolahan berkas, pengujian, debugging, dokumentasi, dan penggunaan GitHub.

Bantuan AI digunakan sebagai pendukung proses pengembangan, pemeriksaan kode, penyusunan pengujian, dan perapian dokumentasi. Kode dan hasil pengujian tetap perlu diperiksa serta dipahami oleh pengembang.