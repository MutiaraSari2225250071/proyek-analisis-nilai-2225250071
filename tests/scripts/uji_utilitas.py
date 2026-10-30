from src.analisis import hitung_statistik
from src.utilitas import susun_laporan


data_siswa = [
    {"nama": "Alya", "nilai": 80.0},
    {"nama": "Bima", "nilai": 70.0},
    {"nama": "Citra", "nilai": 90.0}
]

statistik = hitung_statistik(data_siswa)
laporan = susun_laporan(data_siswa, statistik)

print(laporan)