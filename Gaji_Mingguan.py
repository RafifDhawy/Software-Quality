# Menghitung Gaji Mingguan
def hitung_gaji(jam_kerja, rate_per_jam, pengeluaran):
    jam_normal = 40
    rate_lembur = rate_per_jam * 1.5
    
    if jam_kerja <= jam_normal:
        total_gaji = jam_kerja * rate_per_jam
    else:
        gaji_normal = jam_normal * rate_per_jam
        gaji_lembur = (jam_kerja - jam_normal) * rate_lembur
        total_gaji = gaji_normal + gaji_lembur
    
    return total_gaji

# Menentukan apakah bisa menabung atau tidak
def hitung_tabungan(gaji, pengeluaran):
    if gaji > pengeluaran:
        tabungan = gaji - pengeluaran
        print(f"Bisa Menabung. Tabungan: Rp {tabungan:.2f}")
    elif gaji == pengeluaran:
        print("Tidak Bisa Menabung")
    else:
        print("Cari Tambahan")

# Nilai variabel (input) untuk kasus ini
jam_kerja_minggu_ini = 52  # Variatif, bisa diubah sesuai skenario testing
rate_per_jam = 15000  # Variatif, bisa diubah sesuai skenario testing
pengeluaran_minggu_ini = 600000  # Variatif, bisa diubah sesuai skenario testing

# Hitung Gaji
gaji_minggu_ini = hitung_gaji(jam_kerja_minggu_ini, rate_per_jam, pengeluaran_minggu_ini)
print(f"Total Gaji Minggu Ini: Rp {gaji_minggu_ini:.2f}")

# Hitung apakah bisa menabung atau tidak
hitung_tabungan(gaji_minggu_ini, pengeluaran_minggu_ini)
