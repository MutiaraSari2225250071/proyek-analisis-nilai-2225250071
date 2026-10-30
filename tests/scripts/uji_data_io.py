from src.data_io import baca_data


data_siswa = baca_data("data/nilai_contoh.txt")

print("\nHASIL PEMBACAAN DATA")
print("====================")

for siswa in data_siswa:
    print(f"Nama: {siswa['nama']}, Nilai: {siswa['nilai']}")

print(f"\nJumlah data yang terbaca: {len(data_siswa)}")