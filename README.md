## PACKAGE BINER ##

Package Biner merupakan sebuah package yang dirancang khusus untuk mengubah suatu bilangan bulat dan desimal ke bilangan biner. Fungsi ini juga dapat menganalisis bilangan biner dan melakukan operasi penjumlahan dan logika dasar dengan bilangan biner. Dengan fungsi ini, pengguna dapat dengan mudah mengonversi dan menganalisis serta melakukan operasi penjumlahan dan logika dasar bilangan biner.

## FITUR UTAMA ##
1. Konversi bilangan. Fungsi ini dapat mengonversi bilangan bulat ke biner dan sebaliknya.
2. Operasi Dasar Bilangan Biner. Fungsi ini dapat melakukan operasi penjumlahan, pengurangan, perkalian, dan pembagian dengan menginputkan bilangan bulat kemudian mengoperasikan bilangan biner dari bilangan bulat yang dimasukkan.
3. Operasi logika. Fungsi ini dapat mengoperasikan bilangan biner menggunakan AND, OR, XOR, dan NOT.
4. penggantian dan pencarian. Fungsi ini dapat mencari dan mengganti bagian dari representasi biner, seperti mengganti bit tertentu dengan nilai baru.
5. Manipulasi Bit. Fungsi ini dapat melakukan operasi manipulasi Bit, seperti penggeseran dan pembalikan.
6. Analisis dan Statistik. Fungsi ini dapat menganalisis bilangan biner, seperti menghitung jumlah bit yang disetel.

## INSTALASI ##
Langkah-langkah Install Package biner di Pip

1. Pastikan Python dan Pip Terinstal
Sebelum menginstall package, pastikan Anda sudah menginstal Python dan pip di sistem Anda. Untuk memeriksa apakah sudah terinstal, buka terminal atau command prompt dan jalankan perintah berikut:
```
python --version
pip --version
```

2. Install Package biner
Setelah memastikan Python dan pip sudah terpasang, Anda dapat menginstall package biner dengan perintah berikut di terminal:
```
pip install biner
```

3. Verifikasi Installasi
Setelah proses instalasi selesai, Anda bisa memverifikasi apakah package biner sudah terinstal dengan menjalankan perintah berikut:
```
pip show biner
```

## CARA PENGGUNAAN ##
Untuk menggunakan package ini, pastikan Anda sudah mengimpor package biner ke dalam kode Python Anda:
```
import biner
```
1. Modul Konversi
Modul ini menyediakan fungsi untuk mengonversi bilangan biner ke integer dan bilangan bulat ke biner.
Fungsi:
  - binertointeger(bil_biner)
  - bulat_ke_biner(bil_bulat)
Contoh penggunaan:
```
hasil = biner.binertointeger(1101)
print(hasil)  # Output: 13
```

2. Modul Operasi
Modul ini menyediakan fungsi untuk operasi aritmatika dasar pada bilangan biner yang dihasilkan dari bilangan bulat.
Fungsi:
  - binary_addition_from_int(a, b)
  - binary_subtraction_from_int(a, b)
  - binary_multiplication_from_int(a, b)
  - binary_division_from_int(a, b)
contoh penggunaan:
```
hasil = biner.binary_multiplication_from_int(2, 3)
print(hasil)  # Output: 110
```

3. Modul Operasi Logika
Modul ini menyediakan fungsi untuk operasi logika pada bilangan biner.
Fungsi:
  - operasi_and(a, b)
  - operasi_or(a, b)
  - operasi_xor(a, b)
  - operasi_not(a)
contoh penggunaan:
```
hasil = biner.operasi_and(13, 15)
print(hasil)   # output : 1101
```

4. Modul Ganti dan Cari Bit
Modul ini menyediakan fungsi untuk mengganti dan mencari bit pada posisi tertentu.
Fungsi:
  - ganti_bit(n, pos, nilai)
  - cari_bit(biner_str, pos)
contoh penggunaan:
```
hasil = biner.ganti_bit(10, 2, 1)
print(hasil)   # output : 1110
```





