from src.data_io import baca_data
from src.analisis import validasi_nilai, hitung_statistik
from src.utilitas import susun_laporan

data = baca_data("data/uji_tc08.txt")
data_valid = [
    siswa for siswa in data
    if validasi_nilai(siswa["nilai"])
]

statistik = hitung_statistik(data_valid)
laporan = susun_laporan(data_valid, statistik, kkm=75)

print(laporan)
