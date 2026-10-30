import unittest

from src.data_io import baca_data
from src.analisis import hitung_statistik, validasi_nilai
from src.utilitas import susun_laporan


class TestTC01(unittest.TestCase):
    def test_data_normal(self):
        data_siswa = baca_data("data/uji_tc01.txt")
        data_valid = [
            siswa for siswa in data_siswa
            if validasi_nilai(siswa["nilai"])
        ]

        statistik = hitung_statistik(data_valid)
        laporan = susun_laporan(data_valid, statistik, kkm=75)

        self.assertEqual(statistik["jumlah_data"], 3)
        self.assertAlmostEqual(statistik["rata_rata"], 80.0)
        self.assertEqual(statistik["nilai_tertinggi"], 90)
        self.assertEqual(statistik["nilai_terendah"], 70)
        self.assertIn("2", laporan)
        self.assertIn("1", laporan)


if __name__ == "__main__":
    unittest.main()