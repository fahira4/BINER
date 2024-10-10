# Fungsi untuk mengonversi bilangan desimal ke biner
def desimal_ke_biner(desimal):
    return bin(desimal)[2:]  # Menghapus prefix '0b'

# Fungsi operasi AND
def operasi_and(bil1, bil2):
    hasil_and = bil1 & bil2
    return desimal_ke_biner(hasil_and), hasil_and

# Fungsi operasi OR
def operasi_or(bil1, bil2):
    hasil_or = bil1 | bil2
    return desimal_ke_biner(hasil_or), hasil_or

# Fungsi operasi XOR
def operasi_xor(bil1, bil2):
    hasil_xor = bil1 ^ bil2
    return desimal_ke_biner(hasil_xor), hasil_xor

# Fungsi operasi NOT
def operasi_not(bil):
    hasil_not = ~bil
    # Menambahkan padding hanya di sini
    biner_hasil = format(hasil_not & 0b1111, '04b')  # 4 bit padding
    return biner_hasil, hasil_not







