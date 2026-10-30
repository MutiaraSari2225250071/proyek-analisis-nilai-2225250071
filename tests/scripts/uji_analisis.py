from src.analisis import (
    validasi_nilai,
    hitung_statistik,
    tentukan_status
)


print("HASIL PENGUJIAN MODUL ANALISIS")
print("==============================")

# Pengujian validasi nilai
print("\n1. PENGUJIAN VALIDASI NILAI")

nilai_uji = [0, 75, 100, -1, 101]

for nilai in nilai_uji:
    print(f"Nilai {nilai}: {validasi_nilai(nilai)}")


# Pengujian statistik
print("\n2. PENGUJIAN STATISTIK")

data_siswa = [
    {"nama": "Alya", "nilai": 80.0},
    {"nama": "Bima", "nilai": 70.0},
    {"nama": "Citra", "nilai": 90.0}
]

statistik = hitung_statistik(data_siswa)

print(f"Jumlah data: {statistik['jumlah_data']}")
print(f"Rata-rata: {statistik['rata_rata']:.2f}")
print(f"Nilai tertinggi: {statistik['nilai_tertinggi']}")
print(f"Nilai terendah: {statistik['nilai_terendah']}")


# Pengujian status ketuntasan
print("\n3. PENGUJIAN STATUS KETUNTASAN")

for siswa in data_siswa:
    status = tentukan_status(siswa["nilai"])
    print(f"{siswa['nama']}: {siswa['nilai']} - {status}")


# Pengujian data kosong
print("\n4. PENGUJIAN DATA KOSONG")

print(f"Statistik data kosong: {hitung_statistik([])}")