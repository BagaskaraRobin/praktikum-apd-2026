# program login 

nama = "robin"
sandi = "68"

username = input("Masukkan username: ").lower().strip()
password = input("Masukkan password: ").lower().strip()

if username == nama:
    if password == sandi:
        print("login berhasil, selamat datang", nama)
    else:
        print("username atau password salah")
        exit()
else: 
    print("username atau password salah")
    exit()



# program utama
 # Rokie: poin < 100
 # Warrior: poin > 100 and poin < 299
 # Master: poin > 300 and poin < 999
 # Grand Master:  poin > 1000 or poin < 4999
 # Legend: poin > 5000 

total_point = int(input("Masukkan point anda: "))


if total_point < 0:
    print("Point tidak vaild, point tidak boleh negatif")
    exit()
else:
    if total_point < 100:
        rank = "Rokie"
        next_rank = 100
    elif total_point >= 100 and total_point <= 299:
        rank = "Warrior"
        next_rank = 300
    elif total_point >= 300 and total_point <= 999:
        rank = "Master"
        next_rank = 1000
    elif total_point >= 1000 and total_point <= 4999:
        rank = "Grand Master"
        next_rank = 5000
    elif total_point >= 5000:
        rank = "Legend"
        next_rank = None

print("Username: ", username)
print("Rank: ", rank)

if next_rank is not None:
    sisa_point = next_rank - total_point
    print(("point untuk rank berikut: "), sisa_point)
else:
    over_point = total_point - 5000
    print("Sudah mencapai rank tertinggi, point lebih: ", over_point)
