from .data_io import baca_data, simpan_laporan
from .analisis import validasi_nilai, hitung_statistik
from .utilitas import susun_laporan


def main():
    """Menjalankan program rekap dan analisis nilai matematika."""
    lokasi_data = "data/nilai_contoh.txt"
    lokasi_laporan = "output/laporan_analisis.txt"
    kkm = 75

    print("=" * 45)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA")
    print("=" * 45)

    data_siswa = baca_data(lokasi_data)

    data_valid = []

    for siswa in data_siswa:
        if validasi_nilai(siswa["nilai"]):
            data_valid.append(siswa)
        else:
            print(
                f"Data {siswa['nama']} dilewati: "
                f"nilai {siswa['nilai']:g} berada di luar rentang 0-100."
            )

    if not data_valid:
        print("\nTidak terdapat data nilai valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data_valid)
    laporan = susun_laporan(data_valid, statistik, kkm)

    print()
    print(laporan)

    simpan_laporan(lokasi_laporan, laporan)


if __name__ == "__main__":
    main()