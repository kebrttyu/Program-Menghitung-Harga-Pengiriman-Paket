# ============================================
# APLIKASI PENGHITUNG BIAYA PENGIRIMAN PAKET
# Rute: Jakarta - Surabaya
# ============================================

print("=" * 50)
print("APLIKASI PENGHITUNG BIAYA PENGIRIMAN")
print("PAKET JAKARTA - SURABAYA")
print("Catatan: Tarif berlaku untuk rute Jakarta ke Surabaya.")
print("Tarif rute lain akan berbeda.")
print("=" * 50)

nama_pengirim = input("Nama Pengirim : ")
nama_penerima = input("Nama Penerima : ")
no_hp = input("No. HP : ")

print("-" * 50)

berat = float(input("Berat Paket (kg): "))
panjang = float(input("Panjang (cm): "))
lebar = float(input("Lebar (cm): "))
tinggi = float(input("Tinggi (cm): "))

berat_volume = (panjang * lebar * tinggi) / 6000
berat_volume = int(berat_volume)

if berat_volume > berat:
    berat_tagih = berat_volume
    jenis_berat = "Volume"
else:
    berat_tagih = berat
    jenis_berat = "Aktual"

print("\nBerat Aktual :", berat, "kg")
print("Berat Volume :", berat_volume, "kg")
print("Berat Tagih  :", berat_tagih, "kg (" + jenis_berat + ")")

print("-" * 50)
print("Jenis Layanan (Rute Jakarta - Surabaya):")
print("1. Reguler (Rp 12.000/kg, 3-4 hari)")
print("2. Express (Rp 20.000/kg, 1-2 hari)")
print("3. Same Day (Rp 35.000/kg, hari ini)")

layanan = input("Pilih Layanan (1/2/3) : ")

if layanan == "1":
    nama_layanan = "Reguler"
    tarif_per_kg = 12000
    estimasi = "3-4 hari kerja"
elif layanan == "2":
    nama_layanan = "Express"
    tarif_per_kg = 20000
    estimasi = "1-2 hari kerja"
elif layanan == "3":
    nama_layanan = "Same Day"
    tarif_per_kg = 35000
    estimasi = "Hari ini"
else:
    nama_layanan = "Reguler"
    tarif_per_kg = 12000
    estimasi = "3-4 hari kerja"

print("\nJenis Paket:")
print("1. Dokumen")
print("2. Elektronik")
print("3. Makanan / Fragile")
print("4. Paket Biasa")

jenis = input("Pilih Jenis (1/2/3/4) : ")

if jenis == "1":
    nama_jenis = "Dokumen"
    biaya_jenis = 2000
elif jenis == "2":
    nama_jenis = "Elektronik"
    biaya_jenis = 10000
elif jenis == "3":
    nama_jenis = "Makanan / Fragile"
    biaya_jenis = 8000
else:
    nama_jenis = "Paket Biasa"
    biaya_jenis = 0

biaya_pengiriman = int(berat_tagih * tarif_per_kg)
total_biaya = biaya_pengiriman + biaya_jenis

asuransi = input("\nGunakan Asuransi? (Y/T) : ")

if asuransi.upper() == "Y":
    nilai_barang = float(input("Nilai Barang (Rp) : "))

    if nilai_barang >= 1000000:
        biaya_asuransi = int(nilai_barang * 0.002)

        if nilai_barang >= 5000000:
            ket_asuransi = "Asuransi Premium"
        else:
            ket_asuransi = "Asuransi Standar"
    else:
        biaya_asuransi = 3000
        ket_asuransi = "Asuransi Minimal"
else:
    biaya_asuransi = 0
    ket_asuransi = "Tanpa Asuransi"

total_biaya += biaya_asuransi

print("\n" + "=" * 50)
print("STRUK PENGIRIMAN PAKET")
print("Jakarta - Surabaya")
print("=" * 50)

print("Pengirim     :", nama_pengirim)
print("Penerima     :", nama_penerima)
print("No. HP       :", no_hp)
print("Rute         : Jakarta - Surabaya")

print("-" * 50)

print("Berat Tagih  :", berat_tagih, "kg")
print("Jenis Paket  :", nama_jenis)
print("Layanan      :", nama_layanan)
print("Estimasi     :", estimasi)

print("-" * 50)

print("Biaya Kirim  : Rp", biaya_pengiriman)
print("Biaya Jenis  : Rp", biaya_jenis)
print("Asuransi     : Rp", biaya_asuransi, "(" + ket_asuransi + ")")

print("-" * 50)

print("TOTAL BIAYA  : Rp", total_biaya)

if total_biaya <= 30000:
    kategori = "MURAH"

    if layanan == "1":
        pesan = "Pilihan ekonomis, cocok untuk paket biasa."
    else:
        pesan = "Biaya terjangkau untuk layanan cepat!"

elif total_biaya <= 75000:
    kategori = "SEDANG"

    if jenis == "2":
        pesan = "Wajar untuk pengiriman elektronik."
    else:
        pesan = "Biaya pengiriman normal."

else:
    kategori = "MAHAL"

    if asuransi.upper() == "Y":
        pesan = "Biaya tinggi karena asuransi & layanan premium."
    else:
        pesan = "Pertimbangkan layanan Reguler untuk hemat biaya."

print("Kategori Biaya :", kategori)
print("Info           :", pesan)

print("=" * 50)
print("*Tarif hanya berlaku untuk rute Jakarta-Surabaya")
print("*Tarif rute lain berbeda sesuai jarak & zona")
print("=" * 50)

print("\nTerima kasih telah menggunakan")
print("Aplikasi Penghitung Biaya Pengiriman!")
print("=" * 50)