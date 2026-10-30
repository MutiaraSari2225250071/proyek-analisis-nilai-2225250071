from src.data_io import baca_data
from src.analisis import hitung_statistik, validasi_nilai
from src.utilitas import susun_laporan

data_siswa = baca_data("data/uji_tc01.txt")
data_valid = [
    siswa for siswa in data_siswa
    if validasi_nilai(siswa["nilai"])
]

statistik = hitung_statistik(data_valid)
laporan = susun_laporan(data_valid, statistik, kkm=75)

print(laporan)
