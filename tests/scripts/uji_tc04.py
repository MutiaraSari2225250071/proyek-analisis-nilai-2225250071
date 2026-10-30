import unittest

from src.analisis import validasi_nilai


class TestTC04(unittest.TestCase):
    def test_nilai_di_luar_dan_batas_rentang(self):
        self.assertFalse(validasi_nilai(105))
        self.assertTrue(validasi_nilai(100))
        self.assertTrue(validasi_nilai(0))
        self.assertFalse(validasi_nilai(-1))


if __name__ == "__main__":
    unittest.main()