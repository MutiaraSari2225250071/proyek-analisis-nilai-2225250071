def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada pada rentang 0 sampai 100."""
    if not isinstance(nilai, (int, float)) or isinstance(nilai, bool):
        return False

    return 0 <= nilai <= 100


def hitung_statistik(data_siswa):
    """Menghitung statistik dasar dari data nilai yang valid."""
    if not data_siswa:
        return None

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    jumlah_data = len(daftar_nilai)
    nilai_rata_rata = sum(daftar_nilai) / jumlah_data
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    return {
        "jumlah_data": jumlah_data,
        "rata_rata": nilai_rata_rata,
        "nilai_tertinggi": nilai_tertinggi,
        "nilai_terendah": nilai_terendah
    }


def tentukan_status(nilai, kkm=75):
    """Menentukan status ketuntasan berdasarkan nilai KKM."""
    if not validasi_nilai(nilai):
        raise ValueError("Nilai harus berada pada rentang 0 sampai 100.")

    if nilai >= kkm:
        return "Tuntas"

    return "Belum Tuntas"