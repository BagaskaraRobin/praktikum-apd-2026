#if statement

# if konisi:
#     perintah jika kondisinya True

cuaca = "hujan"
if cuaca =="hujan":
    print("bawa payung/jas hujan")
    print("telat dikit")

print("otw kampus")

#if else statement

# if kondisi:
#     perintah jika kondisinya bernilai True
# else:
#     perintah jika kondisinya bernilai False

budget = 50000
cuaca = "cerah"

if budget > 30000 and cuaca == "cerah":
    print("jalan-jalan")
else:
    print("womp womp")

kendaraan = input("Masukkan kendaraan anda: ").lower().strip()

# if elif else statement

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000

print("Tarif parkir:", tarif_parkir)

bilangan = -5
status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("bilangan adalah:", status)

# nested if

username = input("Masukkan username: ").lower().strip()
password = input("Masukkan password: ").lower().strip()

if username == "robin":
    if password == "068":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username salah atau password salah")

angka = 10 / 6
print(f"angka {angka:.02f}")

