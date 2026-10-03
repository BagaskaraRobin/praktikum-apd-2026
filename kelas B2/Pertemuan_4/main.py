batas = 5
for i in range(batas):
    print("Perulangan ke-", i)

game = ["Genshin", 7.0, True]
for i in game:
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(1, 3):
    for j in range(1, 4):
        print(f'{i} x {j} = {i * j}')
    print('')

jawab = "ya"
hitung = 0
while(jawab == "ya"):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")

print(f"Total Perulangan : {hitung}")

for i in range(10):
    if i == 5:
        break
print(i)

angka_benar = 7
while True:
    print("=== Game Tebak angka ===")

    angka_input = int(input("Masukan angka (1-10): "))

    if angka_benar == angka_input:
        print("angka anda benar")
        break
    else:
        print("Angka anda salah")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

saku = int(input("Berapa uang saku awal anda: "))

while saku > 0:
    pengeluaran = int(input("Mau keluar berapa uang anda?:"))
    sisa = saku - pengeluaran
    print("sisa saku anda: ", sisa)