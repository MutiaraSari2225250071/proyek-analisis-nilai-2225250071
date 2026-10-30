# DOKUMENTASI PENGUJIAN PROGRAM

**Nama Program:** Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python

**Rentang nilai valid:** 0–100

**Kriteria Ketuntasan Minimal (KKM):** 75

## TC-01 — Data Nilai Normal

**Tujuan:** Memastikan program dapat membaca data nilai siswa, menghitung statistik dasar, dan menentukan status ketuntasan dengan benar.

**Data masukan:**
```text
Alya,80
Bima,70
Citra,90
```

**Hasil yang diharapkan:**
- Jumlah data valid: 3.
- Nilai rata-rata: 80,00.
- Nilai tertinggi: 90.
- Nilai terendah: 70.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Hasil aktual:**
- Jumlah data valid: 3.
- Nilai rata-rata: 80,00.
- Nilai tertinggi: 90.
- Nilai terendah: 70.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Status:** BERHASIL.

**Kesimpulan:** Program berhasil membaca data normal, menghitung statistik, dan menentukan ketuntasan siswa sesuai hasil yang diharapkan.

## TC-02 — Nilai Minimum 0

**Tujuan:** Memastikan nilai 0 diterima sebagai nilai yang valid.

**Data masukan:**
```text
Alya,0
Bima,80
Citra,100
```

**Hasil yang diharapkan:**
- Nilai 0 dinyatakan valid.
- Jumlah data valid: 3.
- Nilai rata-rata: 60,00.
- Nilai tertinggi: 100.
- Nilai terendah: 0.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Hasil aktual:**
- Validasi nilai 0 menghasilkan `True`.
- Jumlah data valid: 3.
- Nilai rata-rata: 60,00.
- Nilai tertinggi: 100.
- Nilai terendah: 0.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Status:** BERHASIL.

**Kesimpulan:** Program menerima nilai 0 sebagai nilai yang valid dan menghasilkan perhitungan statistik serta status ketuntasan yang sesuai.

## TC-03 — Nilai Maksimum 100

**Tujuan:** Memastikan nilai 100 diterima sebagai nilai valid dan diproses dengan benar oleh program.

**Data masukan:**
```text
Alya,100
Bima,80
Citra,70
```

**Hasil yang diharapkan:**
- Nilai 100 dinyatakan valid.
- Jumlah data valid: 3.
- Nilai rata-rata: 83,33.
- Nilai tertinggi: 100.
- Nilai terendah: 70.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Hasil aktual:**
- Validasi nilai 100 menghasilkan `True`.
- Jumlah data valid: 3.
- Nilai rata-rata: 83,33.
- Nilai tertinggi: 100.
- Nilai terendah: 70.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Status:** BERHASIL.

**Kesimpulan:** Program menerima nilai 100 sebagai nilai valid dan menghasilkan statistik serta status ketuntasan sesuai hasil yang diharapkan.

## TC-04 — Nilai di Luar Rentang

**Tujuan:** Memastikan program menolak nilai yang kurang dari 0 atau lebih dari 100.

**Data pengujian:** 105, 100, 0, dan -1.

**Hasil yang diharapkan:**
- Nilai 105: Tidak valid.
- Nilai 100: Valid.
- Nilai 0: Valid.
- Nilai -1: Tidak valid.

**Hasil aktual:**
- Nilai 105 menghasilkan status Tidak valid.
- Nilai 100 menghasilkan status Valid.
- Nilai 0 menghasilkan status Valid.
- Nilai -1 menghasilkan status Tidak valid.

**Status:** BERHASIL.

**Kesimpulan:** Fungsi validasi berhasil membedakan nilai yang berada di dalam dan di luar rentang 0–100.

## TC-05 — Berkas Tidak Ditemukan

**Tujuan:** Memastikan program dapat menangani kondisi ketika berkas masukan tidak ditemukan.

**Data pengujian:** `data/berkas_tidak_ada.txt` (berkas tidak tersedia).

**Hasil yang diharapkan:**
- Program menampilkan pesan bahwa berkas tidak ditemukan.
- Fungsi `baca_data()` mengembalikan daftar kosong.
- Program tidak mengalami error yang tidak tertangani.

**Hasil aktual:**
- Program menampilkan pesan `Berkas tidak ditemukan: data\berkas_tidak_ada.txt`.
- Data yang terbaca adalah `[]`.
- Status pengujian menunjukkan `BERHASIL`.

**Status:** BERHASIL.

**Kesimpulan:** Program berhasil menangani berkas masukan yang tidak ditemukan dengan menampilkan pesan dan mengembalikan daftar kosong.

## TC-06 — Semua Siswa Tuntas

**Tujuan:** Memastikan program menghitung jumlah siswa tuntas dengan benar ketika seluruh nilai mencapai atau melampaui KKM.

**Data masukan:**
```text
Alya,80
Bima,90
Citra,100
```

**Hasil yang diharapkan:**
- Jumlah data valid: 3.
- Nilai rata-rata: 90,00.
- Nilai tertinggi: 100.
- Nilai terendah: 80.
- Siswa tuntas: 3.
- Siswa belum tuntas: 0.

**Hasil aktual:**
- Jumlah data valid: 3.
- Nilai rata-rata: 90,00.
- Nilai tertinggi: 100.
- Nilai terendah: 80.
- Siswa tuntas: 3.
- Siswa belum tuntas: 0.

**Status:** BERHASIL.

**Kesimpulan:** Program berhasil menentukan bahwa seluruh siswa mencapai KKM 75 dan menghasilkan statistik yang sesuai dengan hasil yang diharapkan.

## TC-07 — Nilai di Bawah dan di Atas KKM

**Tujuan:** Memastikan program menentukan status ketuntasan dengan benar ketika data siswa memiliki nilai di bawah, sama dengan, dan di atas KKM.

**Data masukan:**
```text
Alya,80
Bima,60
Citra,75
```

**Hasil yang diharapkan:**
- Jumlah data valid: 3.
- Nilai rata-rata: 71,67.
- Nilai tertinggi: 80.
- Nilai terendah: 60.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.

**Hasil aktual:**
- Jumlah data valid: 3.
- Nilai rata-rata: 71,67.
- Nilai tertinggi: 80.
- Nilai terendah: 60.
- Siswa tuntas: 2.
- Siswa belum tuntas: 1.
- Nilai 75 dikategorikan tuntas.

**Status:** BERHASIL.

**Kesimpulan:** Program berhasil menentukan status ketuntasan berdasarkan KKM 75, termasuk menetapkan nilai yang sama dengan KKM sebagai tuntas.

## TC-08 — Tidak Ada Data Valid

**Tujuan:** Memastikan program dapat menangani kondisi ketika seluruh data masukan tidak memenuhi kriteria valid untuk dianalisis.

**Data masukan:**
```text
Alya,105
,80
```

**Hasil yang diharapkan:**
- Baris dengan nama kosong dilewati.
- Data dengan nilai di luar rentang 0–100 tidak digunakan dalam analisis.
- Tidak terdapat data valid yang tersisa.
- Program menampilkan pesan bahwa tidak terdapat data nilai valid untuk dianalisis.

**Hasil aktual:**
- Baris 2 dilewati karena nama siswa kosong.
- Data Alya dengan nilai 105 tidak digunakan dalam analisis.
- Program menampilkan pesan bahwa tidak terdapat data nilai valid untuk dianalisis.
- Tidak ada statistik yang dihitung.

**Status:** BERHASIL.

**Kesimpulan:** Program berhasil menangani data masukan yang tidak valid dan menampilkan pesan yang sesuai ketika tidak ada data nilai yang dapat dianalisis.