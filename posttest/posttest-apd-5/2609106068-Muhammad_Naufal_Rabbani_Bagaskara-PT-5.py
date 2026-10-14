import os

# akun admin 
# user : robin
# pw : 68

akun = [
    ("robin", "68", "admin", []),
    ("1", "1", "user", [])
]

katalog = [
    ["Sword", 1],
    ["Bow", 1],
    ["Magic staff", 1],
    ["Pocket C-RAM", 1],
    ["random bs bag", 1],
    ["Health Potion", 1],   
]

max_level = 10

while True:

    # menu
    os.system("cls")
    print("="*5, "Menu", "="*5)
    print("1.  Login")
    print("2. Register")
    print("3. Exit")
    print("="*16)
    pil_menu = input("Pilihan: ")

    # 1. login
    if pil_menu == "1":
        os.system("cls")
        

        print("="*3, "Login", "="*3)
        user = input("Username: ")
        pw = input("Password: ")

        akses = ""
        inv = []
        for u, p, a, i in akun:
                if u == user and p == pw:
                    akses = a
                    inv = i

        if akses == "":
            print("\nUsername atau Password salah")
            input("\nTekan enter untuk kembali")

        # admin
        if akses == "admin":
            while True:
                os.system("cls")
                print("="*2, "Menu Admin", "="*2)
                print("1. Lihat item ")
                print("2. Hapus item")
                print("3. Tambah item")
                print("4. Logout")
                print("="*16)
                pil_admin = input("Pilihan: ")
                nomor = 1

                if pil_admin == "1":
                    os.system("cls")
                    print("= Item yang ada =")
                    for i, l in katalog:
                        print(nomor,".", i)
                        print("Base level", l)
                        nomor += 1
                    input("\nTekan Enter untuk kembali")


                elif pil_admin == "2":
                    os.system("cls")
                    if len(katalog) == 0:
                        print("="*14)
                        print("Katalog kosong")
                    else:
                        print("=","Item mana yang mau di hapus?", "=")

                    for i, l in katalog:
                        print(nomor,".", i)
                        print("Base level", l)
                        nomor += 1

                    pil_hap = input("\nPilihan(Pencet Enter untuk cancel): ")

                    if pil_hap == "":
                        continue

                    if pil_hap.isdigit() and 1 <= int(pil_hap) <= len(katalog):
                        dihapus = katalog.pop(int(pil_hap) - 1)
                        print("\n" + dihapus[0], "dihapus dari katalog")
                    else:
                        print("\nNomor tidak valid!")
                    input("\nTekan Enter untuk kembali")
                    
                elif pil_admin == "3":
                    os.system("cls")
                    print("=", "Tambah Item ke Katalog", "=")
                    nama = input("Nama item: ")
                    base = input("Base level: ")

    
                    sudah_ada = False
                    for n, b in katalog:
                        if n.lower() == nama.strip().lower():
                            sudah_ada = True

                    if nama.strip() == "":
                        print("\nNama item tidak boleh kosong!")
                    elif not base.isdigit() or int(base) < 1:
                        print("\nBase level harus angka minimal 1!")
                    elif sudah_ada:
                        print("\nItem sudah ada di katalog!")
                    else:
                       katalog.append([nama.strip(), int(base)])
                       print("\n" + nama.strip(), "ditambahkan ke katalog")

                    input("\nTekan Enter untuk kembali")

                elif pil_admin == "4":
                    os.system("cls")
                    break
                else:
                    print("\nPilihan tidak valid")
                    input("\nTekan Enter untuk kembali")

        # user
        if akses == "user":
            while True:
                
                os.system("cls")
                print("="*2, "Inventory User", "="*2)
                print("1. Lihat/Add item ")
                print("2. Upgrade item")
                print("3. Buang item")
                print("4. Logout")
                print("="*20)
                pil_user = input("Pilihan: ")
                
                if pil_user == "1":
                    os.system("cls")

                    print("= Inventory kamu =")
                    if len(inv) == 0:
                        print("Inventory kosong")
                    else:
                        for nomor, (nama, base, sekarang) in enumerate(inv, 1):
                            print(nomor, ".", nama)
                            print("    Base level:", base)
                            print("    Level sekarang:", sekarang)

                    print("\n= Katalog =")
                    if len(katalog) == 0:
                        print("Katalog kosong")
                        input("\nTekan Enter untuk kembali")
                        continue

                    for nomor, (nama, base) in enumerate(katalog, 1):
                        print(nomor,".", nama)
                        print("    Base level:", base)

                    add = input("\nItem apa yang mau di ambil?(Enter untuk kembali): ")

                    if add == "":
                        continue

                    if add.isdigit() and 1 <= int(add) <= len(katalog):
                        item = katalog[int(add) - 1][0]
                        base = katalog[int(add) - 1][1]
                        inv.append([item, base, base])
                        print("\n" + item, "masuk ke inventory")
                    else:
                        print("\nNomor tidak valid")
                    input("\nTekan Enter untuk kembali")

                elif pil_user == "2":
                    os.system("cls")

                    if len(katalog) == 0:
                        print("="*14)
                        print("Katalog kosong")
                        continue

                    print("=Item mana yang mau di upgrade?=")
                    for nomor, (item, base, sekarang) in enumerate(inv, 1):
                        print(nomor, ".", item)
                        print("     Level Sekarang:", sekarang, "/", max_level)

                    pil_up = input("Pilihan (Tekan Enter untuk cancel): ")

                    if pil_up == "":
                        continue

                    if pil_up.isdigit() and 1 <= int(pil_up) <= len(inv):
                        item = inv[int(pil_up) - 1]
                        if item[2] >= max_level:
                            print("\n Level item sudah maksimal")
                        else:
                            item[2] += 1
                            print("\n", item[0], "Upgrade sukses")
                    else:
                        print("\nNomor tidak valid")
                    input("\nTekan Enter untuk kembali")
                
                elif pil_user == "3":
                    os.system("cls")

                    if len(inv) == 0:
                        print("Inventory kosong")
                        input("\nTekan Enter untuk kembali")
                        continue

                    print("= Item mana yang mau dibuang? =")
                    for nomor, (nama, base, sekarang) in enumerate(inv, 1):
                        print(nomor,".", nama)
                        print("    Level sekarang:", sekarang)

                    pil_buang = input("\nPilihan (Enter untuk cancel): ")

                    if pil_buang == "":
                        continue

                    if pil_buang.isdigit() and 1 <= int(pil_buang) <= len(inv):
                        dibuang = inv.pop(int(pil_buang) - 1)
                        print("\n" + dibuang[0], "dibuang dari inventory")
                    else:
                        print("\nNomor tidak valid!")
                    input("\nTekan Enter untuk kembali")

                # logout
                elif pil_user == "4":
                    os.system("cls")
                    break

                else:
                    print("\nPilihan tidak valid")
                    input("\nTekan Enter untuk kembali")
                
    elif pil_menu == "2":
        os.system("cls")
        print("="*3, "Register", "="*3)
        user = input("User: ")
        pw = input("Password: ")

        sudah_ada = False
        for u, p, a, i in akun:
            if u == user:
                sudah_ada = True
                break

        if user == "" or pw == "":
            print("\nUsername dan password tidak boleh kosong!")
        elif sudah_ada:
            print("\nUsername sudah dipakai!")
        else:
            akun.append((user, pw, "user", []))
            print("\nRegistrasi berhasil! Silakan login.")
        input("\nTekan Enter untuk kembali")

    elif pil_menu == "3":
        os.system("cls")
        print("Sampai jumpa!")
        break

    else:
        print("\nPilihan tidak valid!")
        input("\nTekan Enter untuk kembali")