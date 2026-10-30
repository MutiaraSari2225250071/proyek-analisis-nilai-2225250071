# PROPOSAL PROYEK PROGRAM SEDERHANA
## Program Rekap dan Analisis Nilai Matematika Kelas

### 1. Judul Proyek

**Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python**

### 2. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan dalam proses pembelajaran. Data nilai perlu direkap dan dianalisis untuk mengetahui hasil belajar siswa, seperti nilai rata-rata, nilai tertinggi, nilai terendah, serta jumlah siswa yang telah mencapai Kriteria Ketuntasan Minimal (KKM).

Apabila pengolahan dilakukan secara manual, proses perhitungan membutuhkan waktu dan berpotensi menimbulkan kesalahan. Oleh karena itu, diperlukan program sederhana yang dapat membantu mengolah data nilai secara lebih sistematis dan menghasilkan informasi yang mudah dipahami.

Melalui proyek ini, dikembangkan program berbasis Python yang berjalan melalui terminal atau konsol. Program dirancang untuk membaca data nilai siswa dari berkas teks, memvalidasi nilai, menghitung statistik dasar, menentukan status ketuntasan, serta menyimpan hasil analisis ke dalam berkas laporan.

Proyek ini juga menjadi sarana penerapan materi Algoritma dan Pemrograman, khususnya penggunaan fungsi, struktur data, pengolahan berkas, validasi masukan, pengujian program, dan dokumentasi proyek.

### 3. Pengguna dan Tujuan Program

#### 3.1 Pengguna Program

Pengguna utama program ini adalah guru matematika atau pihak yang membutuhkan bantuan dalam merekap dan menganalisis nilai matematika siswa.

#### 3.2 Tujuan Program

Program ini memiliki beberapa tujuan sebagai berikut.

1. Membantu pengguna membaca dan mengolah data nilai matematika siswa.
2. Memvalidasi data agar hanya nilai yang memenuhi ketentuan yang digunakan dalam analisis.
3. Menghitung nilai rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status ketuntasan setiap siswa berdasarkan KKM yang ditetapkan.
5. Menghitung jumlah siswa yang tuntas dan belum tuntas.
6. Menampilkan hasil analisis melalui terminal atau konsol.
7. Menyimpan hasil analisis ke dalam berkas laporan teks.
8. Menerapkan pemrograman modular agar program lebih terstruktur, mudah diuji, dan mudah dikembangkan.

### 4. Rumusan Masalah dan Ruang Lingkup

#### 4.1 Rumusan Masalah

Berdasarkan latar belakang tersebut, rumusan masalah dalam proyek ini adalah sebagai berikut.

1. Bagaimana merancang program sederhana untuk membaca dan mengolah data nilai matematika siswa menggunakan Python?
2. Bagaimana menerapkan validasi agar data nilai yang digunakan sesuai dengan ketentuan?
3. Bagaimana menghitung statistik dasar dan menentukan status ketuntasan siswa secara otomatis?
4. Bagaimana menyimpan hasil pengolahan nilai ke dalam berkas laporan agar dapat digunakan kembali?

#### 4.2 Ruang Lingkup Program

Agar pengembangan program tetap terarah, ruang lingkup proyek dibatasi pada hal-hal berikut.

1. Program dikembangkan menggunakan bahasa pemrograman Python.
2. Program dijalankan melalui terminal atau konsol, tanpa antarmuka grafis.
3. Data siswa dibaca dari berkas teks yang berada di dalam folder `data`.
4. Setiap data siswa terdiri atas nama dan nilai matematika.
5. Nilai yang valid berada pada rentang 0 sampai 100, termasuk kedua batas tersebut.
6. Nilai yang berada di luar rentang tersebut tidak digunakan dalam analisis.
7. Program menghitung jumlah data valid, nilai rata-rata, nilai tertinggi, dan nilai terendah.
8. Program menentukan status ketuntasan berdasarkan KKM sebesar 75.
9. Siswa dengan nilai lebih besar atau sama dengan KKM dinyatakan tuntas, sedangkan siswa dengan nilai di bawah KKM dinyatakan belum tuntas.
10. Program menampilkan hasil analisis di terminal atau konsol.
11. Program menyimpan laporan hasil analisis ke dalam berkas teks pada folder `output`.
12. Program menangani kondisi ketika berkas masukan tidak ditemukan atau tidak terdapat data nilai valid.

Fitur seperti antarmuka grafis, basis data, pengelolaan banyak kelas, dan analisis statistik lanjutan tidak termasuk dalam ruang lingkup proyek ini.

### 5. Kebutuhan Program

#### 5.1 User Story

User story yang menjadi dasar perancangan program adalah sebagai berikut.

**Sebagai guru matematika, saya ingin mengolah data nilai siswa secara otomatis agar saya dapat mengetahui statistik nilai dan status ketuntasan siswa dengan lebih mudah, cepat, dan sistematis.**

#### 5.2 Kebutuhan Fungsional

Kebutuhan fungsional menjelaskan fungsi yang harus tersedia dalam program.

- **KF-01:** Program dapat membaca data nama dan nilai siswa dari berkas teks.
- **KF-02:** Program dapat memeriksa apakah nilai berupa angka dan berada pada rentang 0–100.
- **KF-03:** Program dapat mengabaikan data yang tidak valid dan memberikan informasi mengenai data tersebut.
- **KF-04:** Program dapat menghitung jumlah data nilai yang valid.
- **KF-05:** Program dapat menghitung nilai rata-rata, nilai tertinggi, dan nilai terendah.
- **KF-06:** Program dapat menentukan status ketuntasan setiap siswa berdasarkan KKM sebesar 75.
- **KF-07:** Program dapat menghitung jumlah siswa yang tuntas dan belum tuntas.
- **KF-08:** Program dapat menampilkan hasil analisis melalui terminal atau konsol.
- **KF-09:** Program dapat menyimpan hasil analisis ke dalam berkas laporan teks.
- **KF-10:** Program dapat menangani berkas masukan yang tidak ditemukan serta kondisi tidak adanya data nilai valid.

#### 5.3 Kebutuhan Nonfungsional

Kebutuhan nonfungsional menjelaskan karakteristik yang diharapkan dari program.

- **KNF-01 — Kemudahan penggunaan:** Program menampilkan informasi dengan jelas sehingga mudah dipahami pengguna.
- **KNF-02 — Ketepatan hasil:** Perhitungan statistik dan status ketuntasan harus sesuai dengan data valid yang diolah.
- **KNF-03 — Keandalan:** Program menangani masukan yang tidak valid dan kesalahan pembacaan berkas secara terkontrol.
- **KNF-04 — Modularitas:** Program dibagi menjadi beberapa modul dan fungsi dengan tanggung jawab yang jelas.
- **KNF-05 — Kemudahan pemeliharaan:** Kode ditulis secara terstruktur agar mudah diperiksa, diperbaiki, dan dikembangkan.
- **KNF-06 — Dokumentasi:** Proyek dilengkapi dokumentasi penggunaan, rancangan algoritma, dan kasus pengujian.

### 6. Perancangan IPO (Input, Process, Output)

Perancangan IPO digunakan untuk menjelaskan hubungan antara masukan, proses pengolahan, dan keluaran program.

#### 6.1 Input

Masukan program meliputi:

1. Berkas teks `nilai_contoh.txt` yang berisi nama dan nilai siswa.
2. Nama siswa sebagai data bertipe string.
3. Nilai matematika siswa sebagai data numerik.
4. Nilai KKM sebesar 75 yang digunakan sebagai batas ketuntasan.

Format setiap baris pada berkas masukan adalah:

`Nama Siswa,Nilai`

Contoh isi berkas:

```text
Alya,80
Bima,70
Citra,90
Dimas,75
```

#### 6.2 Process

Proses pengolahan data meliputi:

1. Membaca data siswa dari berkas masukan.
2. Memeriksa kelengkapan data nama dan nilai.
3. Memastikan nilai dapat diproses sebagai angka dan berada pada rentang 0–100.
4. Mengumpulkan data yang valid dan memberikan informasi untuk data yang tidak valid.
5. Memeriksa apakah terdapat data nilai valid.
6. Menghitung jumlah data valid, nilai rata-rata, nilai tertinggi, dan nilai terendah.
7. Membandingkan nilai setiap siswa dengan KKM sebesar 75.
8. Menentukan status ketuntasan setiap siswa.
9. Menghitung jumlah siswa yang tuntas dan belum tuntas.
10. Menyusun hasil pengolahan menjadi laporan.
11. Menampilkan hasil analisis dan menyimpan laporan ke dalam berkas teks.

Jika tidak ditemukan data nilai valid, program menampilkan pesan yang sesuai dan tidak melakukan perhitungan statistik.

#### 6.3 Output

Keluaran program meliputi:

1. Informasi mengenai data yang tidak valid, jika ditemukan.
2. Jumlah data nilai valid yang berhasil diolah.
3. Nilai rata-rata matematika siswa.
4. Nilai tertinggi dan nilai terendah.
5. Daftar nama siswa beserta nilai dan status ketuntasannya.
6. Jumlah siswa yang tuntas.
7. Jumlah siswa yang belum tuntas.
8. Laporan hasil analisis dalam bentuk berkas teks pada folder `output`.

### 7. Algoritma dan Pseudocode

Algoritma dirancang menggunakan pendekatan modular. Setiap fungsi memiliki tanggung jawab tertentu sehingga proses pembacaan data, validasi, analisis, penentuan status, dan penyimpanan laporan dapat dikelola secara terpisah.

#### 7.1 Pseudocode Program Utama

```text
ALGORITMA Program_Rekap_Analisis_Nilai

DEKLARASI
    data_siswa : list
    data_valid : list
    kkm : integer
    statistik : dictionary
    laporan : string

DESKRIPSI
    kkm <- 75

    data_siswa <- baca_data("data/nilai_contoh.txt")

    data_valid <- list kosong

    UNTUK setiap siswa dalam data_siswa LAKUKAN
        JIKA validasi_nilai(siswa.nilai) DAN
           nama siswa tidak kosong MAKA
            tambahkan siswa ke data_valid
        JIKA TIDAK
            tampilkan informasi data tidak valid
        AKHIR JIKA
    AKHIR UNTUK

    JIKA data_valid kosong MAKA
        tampilkan "Tidak terdapat data nilai valid."
        SELESAI
    AKHIR JIKA

    statistik <- hitung_statistik(data_valid)

    UNTUK setiap siswa dalam data_valid LAKUKAN
        siswa.status <- tentukan_status(siswa.nilai, kkm)
    AKHIR UNTUK

    laporan <- susun_laporan(data_valid, statistik, kkm)

    tampilkan laporan

    simpan_laporan("output/laporan_analisis.txt", laporan)

SELESAI
```

#### 7.2 Deskripsi Fungsi

**1. `baca_data()`**

Membaca data nama dan nilai dari berkas teks. Data yang berhasil dibaca diteruskan untuk proses validasi dan analisis. Apabila berkas tidak ditemukan, program memberikan informasi yang sesuai.

**2. `validasi_nilai()`**

Memeriksa apakah nilai dapat diproses sebagai angka dan berada pada rentang 0–100. Nilai di luar rentang tersebut dinyatakan tidak valid.

**3. `hitung_statistik()`**

Menghitung jumlah data valid, nilai rata-rata, nilai tertinggi, dan nilai terendah dari data yang telah lolos validasi.

**4. `tentukan_status()`**

Membandingkan nilai siswa dengan KKM. Jika nilai lebih besar atau sama dengan 75, statusnya adalah *Tuntas*. Jika nilai kurang dari 75, statusnya adalah *Belum Tuntas*.

**5. `susun_laporan()`**

Menyusun data siswa, statistik nilai, dan informasi ketuntasan menjadi teks laporan yang terstruktur.

**6. `simpan_laporan()`**

Menyimpan teks laporan ke dalam berkas `laporan_analisis.txt` pada folder `output`. Jika penyimpanan mengalami kesalahan, program memberikan informasi yang sesuai.

**7. `main()`**

Menjadi fungsi utama yang mengatur urutan pemanggilan fungsi, mulai dari pembacaan data hingga penyimpanan laporan.

### 8. Struktur Program dan Modul

Program dirancang menggunakan pemrograman modular agar setiap bagian memiliki tanggung jawab yang jelas. Struktur direktori yang direncanakan adalah sebagai berikut.

```text
proyek-analisis-nilai/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

Keterangan setiap berkas dan folder:

- **`README.md`**: Berisi deskripsi proyek, tujuan, fitur, cara menjalankan program, format data masukan, dan informasi penggunaan.
- **`proposal.md`**: Berisi dokumen perancangan proyek.
- **`.gitignore`**: Menentukan berkas atau folder yang tidak perlu disertakan dalam repositori Git.
- **`data/`**: Menyimpan berkas masukan yang berisi data nilai siswa.
- **`nilai_contoh.txt`**: Berisi data nama dan nilai yang digunakan untuk menjalankan serta menguji program.
- **`src/`**: Menyimpan kode sumber program.
- **`main.py`**: Berisi fungsi utama yang mengatur alur eksekusi program.
- **`data_io.py`**: Berisi fungsi untuk membaca data masukan dan menyimpan laporan.
- **`analisis.py`**: Berisi fungsi validasi nilai, perhitungan statistik, dan penentuan status ketuntasan.
- **`utilitas.py`**: Berisi fungsi pendukung, seperti penyusunan atau pemformatan teks laporan.
- **`tests/`**: Menyimpan dokumentasi kasus pengujian.
- **`test_case.md`**: Berisi skenario, masukan, hasil yang diharapkan, dan hasil aktual pengujian.
- **`output/`**: Menyimpan laporan hasil analisis.
- **`.gitkeep`**: Menjaga folder `output` tetap tercatat dalam repositori meskipun belum berisi laporan.

Struktur tersebut merupakan rancangan awal. Implementasi setiap fungsi dan penyesuaian teknisnya dilakukan pada tahap pengembangan program.

### 9. Struktur Data

Struktur data utama yang digunakan adalah **list yang berisi dictionary**.

Setiap dictionary mewakili seorang siswa dan menyimpan informasi berupa nama, nilai, serta status ketuntasan setelah proses analisis.

Contoh representasi data:

```python
data_siswa = [
    {"nama": "Alya", "nilai": 80},
    {"nama": "Bima", "nilai": 70},
    {"nama": "Citra", "nilai": 90}
]
```

Setelah status ketuntasan ditentukan, data dapat memuat informasi tambahan:

```python
data_siswa = [
    {"nama": "Alya", "nilai": 80, "status": "Tuntas"},
    {"nama": "Bima", "nilai": 70, "status": "Belum Tuntas"},
    {"nama": "Citra", "nilai": 90, "status": "Tuntas"}
]
```

Struktur data tersebut dipilih karena:

1. **List** dapat menyimpan banyak data siswa dalam satu kumpulan.
2. **Dictionary** memungkinkan setiap informasi siswa diakses menggunakan kunci, seperti `nama`, `nilai`, dan `status`.
3. Data dapat ditambahkan atau diproses secara berurutan menggunakan perulangan.
4. Struktur tersebut memudahkan proses validasi, perhitungan statistik, dan penentuan status ketuntasan.

Selain itu, program menggunakan tipe data string untuk nama siswa dan laporan, serta tipe data numerik untuk nilai dan hasil perhitungan statistik.

### 10. Rancangan Kasus Pengujian

Pengujian dirancang untuk memeriksa apakah program dapat mengolah data secara benar, menangani nilai pada batas yang ditentukan, dan memberikan respons yang sesuai ketika terjadi kesalahan.

#### TC-01 — Data Nilai Normal

**Tujuan:** Memeriksa ketepatan perhitungan statistik dan status ketuntasan pada data yang valid.

- **Masukan:** Alya = 80, Bima = 70, dan Citra = 90.
- **Kondisi:** Semua data memiliki nama dan nilai yang valid.
- **Hasil yang diharapkan:**
  - Jumlah data valid = 3.
  - Nilai rata-rata = 80.
  - Nilai tertinggi = 90.
  - Nilai terendah = 70.
  - Jumlah siswa tuntas = 2.
  - Jumlah siswa belum tuntas = 1.

#### TC-02 — Nilai Batas Minimum

**Tujuan:** Memastikan nilai 0 diterima sebagai nilai yang valid.

- **Masukan:** Alya = 0.
- **Kondisi:** Nama siswa tersedia dan nilai berada pada batas minimum.
- **Hasil yang diharapkan:**
  - Data diterima sebagai data valid.
  - Nilai terendah = 0.
  - Status ketuntasan Alya = Belum Tuntas.

#### TC-03 — Nilai Batas Maksimum

**Tujuan:** Memastikan nilai 100 diterima sebagai nilai yang valid.

- **Masukan:** Bima = 100.
- **Kondisi:** Nama siswa tersedia dan nilai berada pada batas maksimum.
- **Hasil yang diharapkan:**
  - Data diterima sebagai data valid.
  - Nilai tertinggi = 100.
  - Status ketuntasan Bima = Tuntas.

#### TC-04 — Nilai di Luar Rentang

**Tujuan:** Memastikan program menolak nilai yang berada di luar rentang 0–100.

- **Masukan:** Citra = 105.
- **Kondisi:** Nilai lebih besar daripada 100.
- **Hasil yang diharapkan:**
  - Data nilai Citra dinyatakan tidak valid.
  - Program menampilkan informasi mengenai nilai yang tidak valid.
  - Nilai 105 tidak digunakan dalam perhitungan statistik.

#### TC-05 — Berkas Masukan Tidak Ditemukan

**Tujuan:** Memeriksa penanganan kesalahan ketika berkas masukan tidak tersedia.

- **Masukan:** Program diarahkan untuk membaca berkas `data/nilai_contoh.txt` yang tidak ditemukan.
- **Kondisi:** Berkas masukan tidak tersedia pada lokasi yang ditentukan.
- **Hasil yang diharapkan:**
  - Program memberikan pesan bahwa berkas masukan tidak ditemukan.
  - Program tidak berhenti akibat kesalahan yang tidak tertangani.
  - Pengguna memperoleh informasi mengenai kondisi tersebut.

#### TC-06 — Seluruh Siswa Tuntas

**Tujuan:** Memastikan jumlah siswa tuntas dihitung dengan benar ketika seluruh nilai mencapai KKM.

- **Masukan:** Alya = 80, Bima = 85, dan Citra = 90.
- **Kondisi:** Seluruh nilai lebih besar atau sama dengan KKM 75.
- **Hasil yang diharapkan:**
  - Jumlah siswa tuntas = 3.
  - Jumlah siswa belum tuntas = 0.
  - Seluruh siswa memiliki status Tuntas.

#### TC-07 — Data dengan Status Ketuntasan Berbeda

**Tujuan:** Memastikan program dapat menentukan status siswa dengan nilai di bawah dan di atas KKM.

- **Masukan:** Alya = 80, Bima = 60, dan Citra = 75.
- **Kondisi:** Terdapat nilai di bawah KKM dan nilai yang mencapai KKM.
- **Hasil yang diharapkan:**
  - Alya berstatus Tuntas.
  - Bima berstatus Belum Tuntas.
  - Citra berstatus Tuntas.
  - Jumlah siswa tuntas = 2.
  - Jumlah siswa belum tuntas = 1.

#### TC-08 — Tidak Terdapat Data Nilai Valid

**Tujuan:** Memastikan program menangani kondisi ketika tidak ada data yang dapat digunakan untuk analisis.

- **Masukan:** Berkas masukan berisi data yang tidak valid, misalnya `Alya,105` dan `,80`.
- **Kondisi:** Tidak ada data yang memenuhi ketentuan validasi.
- **Hasil yang diharapkan:**
  - Program memberikan informasi mengenai data yang tidak valid.
  - Program menampilkan pesan bahwa tidak terdapat data nilai valid.
  - Program tidak melakukan perhitungan statistik terhadap data kosong.

Kasus pengujian tersebut akan digunakan sebagai acuan pada tahap implementasi dan pengujian. Hasil aktual setiap pengujian dicatat setelah program selesai dibuat dan dijalankan.

### 11. Pembagian Tugas

Proyek ini dikerjakan secara individu. Oleh karena itu, seluruh tanggung jawab perancangan, implementasi, pengujian, dokumentasi, dan pengelolaan repositori dilakukan oleh satu orang.

**Nama:** Mutiara Sari

**NIM:** 2225250071

**Kelas:** 3A

**Program Studi:** Pendidikan Matematika

Pembagian tanggung jawab dalam proyek adalah sebagai berikut.

1. **Perancang proyek:** Menentukan masalah, tujuan, ruang lingkup, kebutuhan, IPO, algoritma, dan struktur program.
2. **Programmer:** Mengimplementasikan kode Python berdasarkan rancangan yang telah dibuat.
3. **Penguji program:** Menjalankan kasus pengujian, memeriksa kesesuaian hasil aktual dengan hasil yang diharapkan, serta memperbaiki kesalahan yang ditemukan.
4. **Penyusun dokumentasi:** Menyusun proposal, README, dokumentasi pengujian, dan laporan hasil pengembangan.
5. **Pengelola repositori:** Mengelola struktur berkas, melakukan pencatatan perubahan menggunakan Git, dan mengunggah proyek ke GitHub.

Seluruh tanggung jawab tersebut dilaksanakan secara bertahap dan saling berkaitan agar proyek dapat dikembangkan secara sistematis.

### 12. Jadwal dan Tahapan Pengerjaan

Pengerjaan proyek direncanakan berdasarkan tahapan pembelajaran pada Pertemuan 14, Pertemuan 15, dan Pertemuan 16.

#### Pertemuan 14 — Perancangan Proyek

Kegiatan yang dilakukan:

1. Menentukan ide dan judul proyek.
2. Menyusun latar belakang, rumusan masalah, tujuan, dan ruang lingkup.
3. Mengidentifikasi pengguna dan kebutuhan program.
4. Menyusun rancangan IPO dan pseudocode.
5. Menentukan fungsi dan pembagian modul.
6. Menentukan struktur data.
7. Menyusun minimal lima kasus pengujian.
8. Menentukan struktur folder dan pembagian tanggung jawab.
9. Menyusun proposal serta menyiapkan repositori proyek.

**Target keluaran:** Proposal proyek, rancangan algoritma, struktur folder, dan rancangan kasus pengujian.

#### Pertemuan 15 — Implementasi, Pengujian, dan Dokumentasi

Kegiatan yang dilakukan:

1. Mengimplementasikan setiap fungsi sesuai dengan rancangan.
2. Mengintegrasikan modul program.
3. Menjalankan program menggunakan data contoh.
4. Melakukan pengujian berdasarkan kasus pengujian yang telah disusun.
5. Memperbaiki kesalahan yang ditemukan.
6. Memastikan keluaran program sesuai dengan hasil yang diharapkan.
7. Menyelesaikan README dan dokumentasi pengujian.

**Target keluaran:** Program yang dapat dijalankan, hasil pengujian, dokumentasi, dan repositori yang diperbarui.

#### Pertemuan 16 — Presentasi dan Evaluasi Proyek

Kegiatan yang dilakukan:

1. Menyiapkan demonstrasi program.
2. Menjelaskan latar belakang, tujuan, dan cara kerja program.
3. Menunjukkan proses pembacaan dan pengolahan data.
4. Menampilkan hasil analisis serta laporan yang dihasilkan.
5. Menjelaskan hasil pengujian dan perbaikan yang dilakukan.
6. Melakukan evaluasi terhadap hasil pengembangan proyek.

**Target keluaran:** Demonstrasi program, penjelasan hasil proyek, dan evaluasi akhir.

Jadwal tersebut merupakan rencana pengerjaan. Pelaksanaannya disesuaikan dengan instruksi dosen dan perkembangan proyek pada setiap pertemuan.

### 13. Repositori Proyek

Repositori proyek digunakan untuk menyimpan kode sumber, dokumentasi, data contoh, dan catatan perubahan selama pengembangan.

Repositori direncanakan menggunakan GitHub dengan informasi berikut.

- **Nama repositori:** `proyek-analisis-nilai-2225250071`
- **Pemilik repositori:** Mutiara Sari
- **Platform:** GitHub
- **Bahasa pemrograman:** Python
- **Tautan repositori:** Akan dicantumkan setelah repositori GitHub dibuat dan berhasil diunggah.

Repositori akan memuat berkas proyek sesuai dengan struktur folder yang telah dirancang. Perubahan selama pengembangan akan dicatat menggunakan Git agar proses pengerjaan dapat ditelusuri secara sistematis.

### Penutup

Program Rekap dan Analisis Nilai Matematika Kelas dirancang sebagai proyek sederhana untuk membantu pengolahan data nilai siswa secara sistematis. Program ini mengintegrasikan pembacaan berkas, validasi data, perhitungan statistik dasar, penentuan status ketuntasan, dan penyimpanan laporan.

Melalui proyek ini, materi Algoritma dan Pemrograman diterapkan dalam bentuk program yang memiliki tujuan jelas, struktur modular, serta rancangan pengujian yang terukur. Rancangan yang telah disusun akan menjadi dasar dalam tahap implementasi, pengujian, dan dokumentasi pada pertemuan berikutnya.