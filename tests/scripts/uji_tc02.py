import unittest

from src.data_io import baca_data
from src.analisis import hitung_statistik, validasi_nilai
from src.utilitas import susun_laporan


class TestTC02(unittest.TestCase):
    def test_nilai_minimum_nol(self):
        data = baca_data("data/uji_tc02.txt")
        data_valid = [
            siswa for siswa in data
            if validasi_nilai(siswa["nilai"])
        ]

        statistik = hitung_statistik(data_valid)
        laporan = susun_laporan(data_valid, statistik, kkm=75)

        self.assertTrue(validasi_nilai(0))
        self.assertEqual(statistik["jumlah_data"], 3)
        self.assertAlmostEqual(statistik["rata_rata"], 60.0)
        self.assertEqual(statistik["nilai_tertinggi"], 100)
        self.assertEqual(statistik["nilai_terendah"], 0)
        self.assertIn("2", laporan)
        self.assertIn("1", laporan)


if __name__ == "__main__":
    unittest.main()
