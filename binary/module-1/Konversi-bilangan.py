Biner = int(input("Masukkan Bilangan Bulat: "))

def bilanganbiner(Biner):
        return bin(Biner).replace("0b", "")

biner = bilanganbiner(Biner)
print(f"Bilangan biner dari {Biner} adalah {biner}")


Bulat = input("Masukkan Bilangan Biner: ")

bilangan_bulat = int(Bulat, 2)

print(f"Bilangan bulat dari Biner {Bulat} adalah {bilangan_bulat}")
