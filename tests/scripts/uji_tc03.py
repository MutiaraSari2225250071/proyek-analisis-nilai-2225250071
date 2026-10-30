from src.data_io import baca_data
from src.analisis import hitung_statistik, validasi_nilai
from src.utilitas import susun_laporan

data = baca_data("data/uji_tc03.txt")
data_valid = [siswa for siswa in data if validasi_nilai(siswa["nilai"])]

print("Validasi nilai 100:", validasi_nilai(100))
print()
print(susun_laporan(data_valid, hitung_statistik(data_valid), kkm=75))
