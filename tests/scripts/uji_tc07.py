import unittest

from src.analisis import hitung_statistik, tentukan_status
from src.utilitas import susun_laporan


class TestTC07(unittest.TestCase):
    def test_nilai_di_sekitar_kkm(self):
        data = [
            {"nama": "Alya", "nilai": 80},
            {"nama": "Bima", "nilai": 60},
            {"nama": "Citra", "nilai": 75},
        ]

        statistik = hitung_statistik(data)
        laporan = susun_laporan(data, statistik, kkm=75)

        self.assertAlmostEqual(statistik["rata_rata"], 71.666666, places=2)
        self.assertEqual(tentukan_status(80), "Tuntas")
        self.assertEqual(tentukan_status(60), "Belum Tuntas")
        self.assertEqual(tentukan_status(75), "Tuntas")
        self.assertIn("2", laporan)
        self.assertIn("1", laporan)


if __name__ == "__main__":
    unittest.main()