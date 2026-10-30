import unittest

from src.data_io import baca_data
from src.analisis import validasi_nilai, hitung_statistik
from src.utilitas import susun_laporan


class TestTC08(unittest.TestCase):
    def test_tidak_ada_data_valid(self):
        data = baca_data("data/uji_tc08.txt")
        data_valid = [
            siswa for siswa in data
            if validasi_nilai(siswa["nilai"])
        ]

        statistik = hitung_statistik(data_valid)
        laporan = susun_laporan(data_valid, statistik, kkm=75)

        self.assertEqual(data_valid, [])
        self.assertIsNone(statistik)
        self.assertIsInstance(laporan, str)


if __name__ == "__main__":
    unittest.main()