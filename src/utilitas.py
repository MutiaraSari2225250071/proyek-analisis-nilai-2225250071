from .analisis import tentukan_status


def susun_laporan(data_siswa, statistik, kkm=75):
    """Menyusun laporan rekap dan analisis nilai siswa."""
    if not data_siswa or statistik is None:
        return "Tidak terdapat data nilai valid untuk dianalisis."

    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    baris_laporan = [
        "=" * 45,
        "LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA",
        "=" * 45,
        f"Jumlah data valid : {statistik['jumlah_data']}",
        f"Nilai rata-rata   : {statistik['rata_rata']:.2f}",
        f"Nilai tertinggi   : {statistik['nilai_tertinggi']:g}",
        f"Nilai terendah    : {statistik['nilai_terendah']:g}",
        f"KKM               : {kkm}",
        "",
        "DAFTAR NILAI DAN STATUS KETUNTASAN",
        "-" * 45,
        f"{'Nama':<20}{'Nilai':>10}  {'Status':<15}",
        "-" * 45
    ]

    for siswa in data_siswa:
        status = tentukan_status(siswa["nilai"], kkm)

        baris_laporan.append(
            f"{siswa['nama']:<20}"
            f"{siswa['nilai']:>10g}  "
            f"{status:<15}"
        )

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    baris_laporan.extend([
        "-" * 45,
        f"Jumlah siswa tuntas       : {jumlah_tuntas}",
        f"Jumlah siswa belum tuntas  : {jumlah_belum_tuntas}",
        "=" * 45
    ])

    return "\n".join(baris_laporan)