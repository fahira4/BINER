def shift_bit(a: int, jumlah_pergeseran: int, arah: str) -> str:
    """
    Menggeser bit dari bilangan bulat ke kiri atau kanan dengan jumlah pergeseran yang ditentukan,
    dan mengembalikan hasil dengan padding minimal 4 digit biner.

    Args:
    - a (int): Bilangan bulat yang akan digeser.
    - jumlah_pergeseran (int): Jumlah bit yang akan digeser.
    - arah (str): Arah pergeseran, 'kiri' atau 'kanan'.

<<<<<<< HEAD
    Returns:
    - str: Representasi biner hasil pergeseran dengan minimal 4 digit.
    """
    if arah == 'kiri':
        hasil_shift = a << jumlah_pergeseran
    elif arah == 'kanan':
        hasil_shift = a >> jumlah_pergeseran
    else:
        raise ValueError("Arah pergeseran harus 'kiri' atau 'kanan'.")
    
    return bin(hasil_shift)[2:].zfill(4)  # Menghilangkan '0b' dan menambahkan padding minimal 4 digit

def inverse_bit(a):
	biner_a = bin(a)[2: ]
	# print(f'Bilangan biner: {biner_a}')
	# # pada bagian ini, bilangan bulat akan diubah ke bilangan biner terlebih dahulu. Jika
	# # bilangannya sudah menjadi biner, maka bilangan tersebut langsung keluar
=======
	biner_a = bin(a)[2: ]
	print(f'Bilangan Biner: {biner_a}')

	# pada bagian ini, bilangan bulat akan diubah ke bilangan biner terlebih dahulu. Jika
	# bilangannya sudah menjadi biner, maka bilangan tersebut langsung keluar

	hasil_shift_left = a << 2 # Hasil: 0b101000 (40)
	# pada bagian ini, bilangan biner tadi akan digeser sebanyak 2 kali ke kiri atau mengkalikan bulat dengan 4
	hasil_shift_right = a >> 2 # Hasil: 0b10 (2)
	# kebalikan dari shift kiri, yaitu membagi bilangan bulat dengan 4

	print(f"Shift kiri: {bin(hasil_shift_left)}")   # Output: '0b101000'
	print(f"Shift kanan: {bin(hasil_shift_right)}") # Output: '0b10'
	# mengeluarkan hasil pergeseran biner. bin berfungsi mengubah kembali bilangan bulat ke biner

def inverse_bit(a):
	biner_a = bin(a)[2: ]
	print(f'Bilangan Biner: {biner_a}')
	# pada bagian ini, bilangan bulat akan diubah ke bilangan biner terlebih dahulu. Jika
	# bilangannya sudah menjadi biner, maka bilangan tersebut langsung keluar
>>>>>>> f062ed2700a098d8cec1b42cc9b296319a2b176a
	bits = biner_a
	# variabel baru untuk membalikkan bilangan biner
	inverse = ''
	# Sengaja dikasi string kosong agar dapat menyimpan hasil inverse biner tadi

	for i in bits:
	# melakukan perulangan tergantung dari jumlah bilangan binernya

		if i == '0':
			inverse += '1'
		# kalau bilangan binernya adalah 0, maka yang disimpan di variabel inverse adalah 1
			
		else:
			inverse += '0'
		# kalau bilangan binernya adalah 1, maka yang disimpan di variabel inverse adalah 1
			
	return int(inverse)

print(inverse_bit(0b1010))