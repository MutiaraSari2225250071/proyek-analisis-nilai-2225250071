import unittest
from unittest.mock import patch

from src.data_io import baca_data


class TestTC05(unittest.TestCase):
    def test_berkas_tidak_ditemukan(self):
        with patch("src.data_io.Path.exists", return_value=False):
            data = baca_data("data/berkas_tidak_ada.txt")

        self.assertEqual(data, [])


if __name__ == "__main__":
    unittest.main()