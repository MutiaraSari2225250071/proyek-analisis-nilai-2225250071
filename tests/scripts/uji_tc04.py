from src.analisis import validasi_nilai

nilai_uji = [105, 100, 0, -1]

for nilai in nilai_uji:
    status = "Valid" if validasi_nilai(nilai) else "Tidak valid"
    print(f"Nilai {nilai}: {status}")
