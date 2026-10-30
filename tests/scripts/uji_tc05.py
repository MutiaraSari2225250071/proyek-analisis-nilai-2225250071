from src.data_io import baca_data

data = baca_data("data/berkas_tidak_ada.txt")

print("Data yang terbaca:", data)
print(
    "Status pengujian:",
    "BERHASIL" if data == [] else "GAGAL"
)
