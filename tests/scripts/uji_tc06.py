import unittest

from src.analisis import hitung_statistik
from src.utilitas import susun_laporan


class TestTC06(unittest.TestCase):
    def test_semua_siswa_tuntas(self):
        data = [
            {"nama": "Alya", "nilai": 80},
            {"nama": "Bima", "nilai": 90},
            {"nama": "Citra", "nilai": 100},
        ]

        statistik = hitung_statistik(data)
        laporan = susun_laporan(data, statistik, kkm=75)

        self.assertEqual(statistik["jumlah_data"], 3)
        self.assertAlmostEqual(statistik["rata_rata"], 90.0)
        self.assertEqual(statistik["nilai_tertinggi"], 100)
        self.assertEqual(statistik["nilai_terendah"], 80)
        self.assertIn("3", laporan)
        self.assertIn("0", laporan)


if __name__ == "__main__":
    unittest.main()