import os

# akun admin 
# user : robin
# pw : 68

akun = {
    "robin":{"password":"68", "akses":"admin","inv":{}},
    "1":{"password":"1", "akses": "user", "inv":{}}
}

katalog = {
    "Sword":1,
    "Bow":1,
    "Magic staff":1,
    "Pocket C-RAM":1,
    "random bs bag":1,
    "Health potion":1
}

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
        inv = {}
        if user in akun and pw == akun[user]["password"]:
            akses = akun[user]["akses"]
            inv = akun[user]["inv"]

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

                if pil_admin == "1":
                    os.system("cls")
                    print("= Item yang ada =")
                    if len(katalog) == 0:
                        print("\nKatalog kosong") 
                    else:
                        for nomor, (nama, base) in enumerate(katalog.items(), 1):
                            print(nomor,".", nama)
                            print("Base level", base)
                        input("\nTekan Enter untuk kembali")


                elif pil_admin == "2":
                    os.system("cls")
                    if len(katalog) == 0:
                        print("="*14)
                        print("Katalog kosong")
                    else:
                        print("=","Item mana yang mau di hapus?", "=")
                        for nomor, (nama, base) in enumerate(katalog.items(), 1):
                            print(nomor,".", nama)
                            print("Base level", base)

                    pil_hap = input("\nPilihan(Pencet Enter untuk cancel): ")

                    if pil_hap == "":
                        continue

                    if pil_hap.isdigit() and 1 <= int(pil_hap) <= len(katalog):
                        nama = list(katalog)[int(pil_hap)-1]
                        katalog.pop(nama)
                        print("\n" + nama, "dihapus dari katalog")
                    else:
                        print("\nNomor tidak valid!")
                    input("\nTekan Enter untuk kembali")
                    
                elif pil_admin == "3":
                    os.system("cls")
                    print("=", "Tambah Item ke Katalog", "=")
                    nama = input("Nama item: ")
                    base = input("Base level: ")

    
                    sudah_ada = False
                    for n in katalog:
                        if n == nama:
                            sudah_ada = True

                    if nama == "":
                        print("\nNama item tidak boleh kosong!")
                    elif not base.isdigit() or int(base) < 1:
                        print("\nBase level harus angka minimal 1!")
                    elif sudah_ada:
                        print("\nItem sudah ada di katalog!")
                    else:
                       katalog[nama] = int(base)
                       print("\n" + nama, "ditambahkan ke katalog")

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
                        for nomor, (nama, base) in enumerate(inv.items(), 1):
                            print(nomor, ".", nama)
                            print("    Base level:", base["base"])
                            print("    Level sekarang:", base["level"])
 
                    print("\n= Katalog =")
                    if len(katalog) == 0:
                        print("Katalog kosong")
                        input("\nTekan Enter untuk kembali")
                        continue

                    for nomor, (nama, base) in enumerate(katalog.items(), 1):
                        print(nomor,".", nama)
                        print("    Base level:", base)

                    add = input("\nItem apa yang mau di ambil?(Enter untuk kembali): ")

                    if add == "":
                        continue

                    if add.isdigit() and 1 <= int(add) <= len(katalog):
                        nama = list(katalog)[int(add) - 1]
                        if nama in inv:
                            print("\n", nama, "sudah ada di inventory")
                        else:
                            base = katalog[nama]
                            inv[nama] = {"base": base, "level":base}
                            print("\n", nama, " masuk ke inventory")
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
                    for nomor, (nama, base) in enumerate(inv.items(), 1):
                        print(nomor, ".", nama)
                        print("     Level Sekarang:", base["level"], "/", max_level)

                    pil_up = input("Pilihan (Tekan Enter untuk cancel): ")

                    if pil_up == "":
                        continue

                    if pil_up.isdigit() and 1 <= int(pil_up) <= len(inv):
                        nama = list(inv)[int(pil_up)-1]
                        if inv[nama]["level"] >= max_level:
                            print("\n Level item sudah maksimal")
                        else:
                            inv[nama]["level"] += 1
                            print("\n", nama, "Upgrade sukses")
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
                    for nomor, (nama, base) in enumerate(inv.items(), 1):
                        print(nomor,".", nama)
                        print("    Level sekarang:", base["level"])

                    pil_buang = input("\nPilihan (Enter untuk cancel): ")

                    if pil_buang == "":
                        continue

                    if pil_buang.isdigit() and 1 <= int(pil_buang) <= len(inv):
                        nama = list(inv)[int(pil_buang) - 1]
                        inv.pop(nama)
                        print("\n" + nama, "dibuang dari inventory")
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

        if user == "" or pw == "":
            print("\nUsername dan password tidak boleh kosong!")
        elif user in akun:
            print("\nUsername sudah dipakai!")
        else:
            akun[user] = {"password":pw, "akses":"user", "inv":{}}
            print("\nRegistrasi berhasil! Silakan login.")
        input("\nTekan Enter untuk kembali")

    elif pil_menu == "3":
        os.system("cls")
        print("Sampai jumpa!")
        break

    else:
        print("\nPilihan tidak valid!")
        input("\nTekan Enter untuk kembali")