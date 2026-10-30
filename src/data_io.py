from pathlib import Path


def baca_data(lokasi_berkas):
    """Membaca data nama dan nilai siswa dari berkas teks."""
    data_siswa = []
    path_berkas = Path(lokasi_berkas)

    try:
        with path_berkas.open("r", encoding="utf-8") as berkas:
            for nomor_baris, baris in enumerate(berkas, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(
                        f"Baris {nomor_baris} dilewati: "
                        "format data tidak sesuai."
                    )
                    continue

                nama = bagian[0].strip()
                nilai_teks = bagian[1].strip()

                if not nama:
                    print(
                        f"Baris {nomor_baris} dilewati: "
                        "nama siswa tidak boleh kosong."
                    )
                    continue

                try:
                    nilai = float(nilai_teks)
                except ValueError:
                    print(
                        f"Baris {nomor_baris} dilewati: "
                        "nilai harus berupa angka."
                    )
                    continue

                data_siswa.append({
                    "nama": nama,
                    "nilai": nilai
                })

    except FileNotFoundError:
        print(f"Berkas tidak ditemukan: {path_berkas}")
        return []

    except OSError as kesalahan:
        print(f"Berkas tidak dapat dibaca: {kesalahan}")
        return []

    return data_siswa


def simpan_laporan(lokasi_berkas, laporan):
    """Menyimpan laporan analisis ke dalam berkas teks."""
    path_berkas = Path(lokasi_berkas)

    try:
        path_berkas.parent.mkdir(parents=True, exist_ok=True)

        with path_berkas.open("w", encoding="utf-8") as berkas:
            berkas.write(laporan)

        print(f"Laporan berhasil disimpan di: {path_berkas}")

    except OSError as kesalahan:
        print(f"Laporan gagal disimpan: {kesalahan}")