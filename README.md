# Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python

## 1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python merupakan program sederhana untuk membaca data nilai siswa, memvalidasi nilai, menghitung statistik dasar, menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), dan menyimpan hasil analisis ke dalam berkas laporan.

Proyek ini dikembangkan sebagai implementasi materi Algoritma dan Pemrograman, khususnya penggunaan fungsi, pengolahan data, validasi masukan, penanganan berkas, serta pengujian program.

## 2. Tujuan Program

Program ini bertujuan untuk:
1. Membaca data nama dan nilai siswa dari berkas teks.
2. Memvalidasi nilai agar berada pada rentang 0 sampai 100.
3. Menghitung jumlah data valid, nilai rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status ketuntasan siswa berdasarkan KKM.
5. Menampilkan hasil analisis dalam bentuk laporan.
6. Menyimpan laporan analisis ke dalam berkas teks.

## 3. Teknologi yang Digunakan

- Bahasa pemrograman: Python.
- Format data masukan: berkas teks (`.txt`).
- Format laporan: berkas teks (`.txt`).
- Editor kode: Visual Studio Code.

## 4. Struktur Proyek

```text
proyek-analisis-nilai-2225250071/
├── data/
│   └── nilai_contoh.txt
├── output/
│   ├── .gitkeep
│   └── laporan_analisis.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
├── proposal.md
├── README.md
└── .gitignore
```

Berkas pengujian sementara yang masih berada di direktori utama akan dirapikan pada tahap berikutnya. Struktur di atas merupakan struktur tujuan dokumentasi.

## 5. Format Data Masukan

Data nilai siswa disimpan dalam berkas `data/nilai_contoh.txt`. Setiap baris berisi nama siswa dan nilai yang dipisahkan dengan tanda koma.

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
- Baris kosong atau data dengan format yang tidak sesuai akan dilewati.
- KKM yang digunakan dalam program adalah 75.

## 6. Cara Menjalankan Program

Pastikan Python sudah terpasang dan terminal berada di direktori utama proyek.

Jalankan perintah berikut pada PowerShell:

```powershell
& "C:\Users\USER\.local\bin\python3.14.exe" -m src.main
```

Program akan membaca data dari `data/nilai_contoh.txt`, menampilkan hasil analisis pada terminal, dan menyimpan laporan ke `output/laporan_analisis.txt`.

Catatan: perintah di atas menggunakan lokasi Python pada komputer pengembang. Jika program dijalankan di komputer lain, sesuaikan perintahnya dengan instalasi Python yang tersedia.

## 7. Hasil Program

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

## 8. Pembagian Modul Program

- `src/main.py`: mengatur alur utama program, memanggil fungsi pembacaan data, validasi, analisis, dan penyusunan laporan.
- `src/data_io.py`: membaca data siswa dari berkas teks dan menyimpan laporan.
- `src/analisis.py`: memvalidasi nilai, menghitung statistik dasar, dan menentukan status ketuntasan.
- `src/utilitas.py`: menyusun hasil analisis menjadi laporan yang mudah dibaca.
- `tests/test_case.md`: mendokumentasikan skenario, hasil yang diharapkan, hasil aktual, dan status pengujian.

## 9. Pengujian Program

Pengujian didokumentasikan dalam `tests/test_case.md`, yang mencakup delapan skenario:
1. Data nilai normal.
2. Nilai minimum 0.
3. Nilai maksimum 100.
4. Nilai di luar rentang.
5. Berkas tidak ditemukan.
6. Semua siswa tuntas.
7. Nilai di bawah dan di atas KKM.
8. Tidak ada data valid.

Hasil pengujian dicatat berdasarkan pelaksanaan pengujian yang telah dilakukan.

## 10. Pengembangan Selanjutnya

Program dapat dikembangkan lebih lanjut dengan menambahkan antarmuka pengguna, pengurutan nilai, pencarian nama siswa, atau ekspor laporan ke format lain.