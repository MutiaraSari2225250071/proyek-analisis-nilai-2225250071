import unittest

from src.data_io import baca_data
from src.analisis import hitung_statistik, validasi_nilai
from src.utilitas import susun_laporan


class TestTC03(unittest.TestCase):
    def test_nilai_maksimum_seratus(self):
        data = baca_data("data/uji_tc03.txt")
        data_valid = [
            siswa for siswa in data
            if validasi_nilai(siswa["nilai"])
        ]

        statistik = hitung_statistik(data_valid)
        laporan = susun_laporan(data_valid, statistik, kkm=75)

        self.assertTrue(validasi_nilai(100))
        self.assertEqual(statistik["jumlah_data"], 3)
        self.assertAlmostEqual(statistik["rata_rata"], 83.333333, places=2)
        self.assertEqual(statistik["nilai_tertinggi"], 100)
        self.assertEqual(statistik["nilai_terendah"], 70)
        self.assertIn("2", laporan)
        self.assertIn("1", laporan)


if __name__ == "__main__":
    unittest.main()