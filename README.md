Aplikasi Penghitung Biaya Pengiriman Paket

Program Python sederhana untuk menghitung biaya pengiriman paket berdasarkan berat aktual, berat volume, jenis layanan, jenis paket, dan pilihan asuransi.

Fitur
Input data pengirim dan penerima
Perhitungan berat volume otomatis
Menentukan berat tagih berdasarkan berat aktual atau berat volume
Pilihan layanan pengiriman:
Reguler
Express
Same Day
Pilihan jenis paket:
Dokumen
Elektronik
Makanan / Fragile
Paket Biasa
Perhitungan biaya asuransi
Menampilkan struk pengiriman lengkap
Kategori biaya pengiriman (Murah, Sedang, Mahal)
Rumus Berat Volume

Berat volume dihitung menggunakan rumus:

(Panjang × Lebar × Tinggi) / 6000

Berat tagih yang digunakan adalah nilai terbesar antara:

Berat aktual
Berat volume
Tarif Pengiriman
Layanan	Tarif per Kg	Estimasi
Reguler	Rp12.000	3-4 Hari Kerja
Express	Rp20.000	1-2 Hari Kerja
Same Day	Rp35.000	Hari Ini
Cara Menjalankan Program
Pastikan Python sudah terinstall.
Clone repository:
git clone https://github.com/username/nama-repository.git
Masuk ke folder project:
cd nama-repository
Jalankan program:
python pengiriman.py
Contoh Penggunaan

Input:

Nama Pengirim : Kevin
Nama Penerima : Budi
Berat Paket : 5
Panjang : 50
Lebar : 30
Tinggi : 20

Output:

Berat Aktual : 5 kg
Berat Volume : 5 kg
Berat Tagih  : 5 kg
TOTAL BIAYA  : Rp 62000

Kevin Herlambang
