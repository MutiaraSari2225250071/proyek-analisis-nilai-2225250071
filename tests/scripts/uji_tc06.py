from src.analisis import hitung_statistik
from src.utilitas import susun_laporan

data = [
    {"nama": "Alya", "nilai": 80},
    {"nama": "Bima", "nilai": 90},
    {"nama": "Citra", "nilai": 100},
]

statistik = hitung_statistik(data)
laporan = susun_laporan(data, statistik, kkm=75)

print(laporan)
