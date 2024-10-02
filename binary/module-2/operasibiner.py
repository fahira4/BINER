# Fungsi untuk mengonversi bilangan bulat ke biner
def int_to_binary(num):
    return bin(num)[2:]  # [2:] untuk menghilangkan prefiks '0b'

# Fungsi untuk penjumlahan biner dari bilangan bulat
def binary_addition_from_int(a, b):
    return int_to_binary(a + b)
 
# Fungsi untuk pengurangan biner dari bilangan bulat
def binary_subtraction_from_int(a, b):
    return int_to_binary(a - b)

# Fungsi untuk perkalian biner dari bilangan bulat
def binary_multiplication_from_int(a, b):
    return int_to_binary(a * b)

# Fungsi untuk pembagian biner dari bilangan bulat
def binary_division_from_int(a, b):
    return int_to_binary(a // b)
