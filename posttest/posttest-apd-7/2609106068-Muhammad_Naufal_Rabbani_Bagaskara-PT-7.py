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

# prosedur

def bersihkan_layar():
    os.system("cls")

def tekan_enter():
    try:
        input("\nTekan Enter untuk kembali")
    except (KeyboardInterrupt):
        pass

def list_katalog():
    if len(katalog) == 0:
        return
    for nomor, (nama, base) in enumerate(katalog.items(), 1):
        print(nomor, ".", nama)
        print("     Base level:", base)

def inventory(inv):
    if len(inv) == 0:
        print("Inventory kosong")
    else:
        for nomor, (nama, base) in enumerate(inv.items(), 1):
            print(nomor, ".", nama)
            print("    Base level:", base["base"])
            print("    Level sekarang:", base["level"])

# fungsi tanpa parameter

def input_menu():
    return input("Pilihan: ")

def jumlah_item_katalog():
    return len(katalog)

#fungsi dengan parameter

def cek_login(username, password):
    if username in akun and password == akun[username]["password"]:
        return akun[username]["akses"]
    return ""

def input_angka(pesan, minimal, maksi):
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                return None
            angka = int(teks)  # bisa memunculkan ValueError
            if angka < minimal or angka > maksi:
                raise ValueError("di luar rentang")
            return angka
        except ValueError:
            print("Input tidak valid! Masukkan angka", minimal, "-", maksi)
        except (KeyboardInterrupt):
            print("\nInput dibatalkan")
            return None

#fungsi rekursif

def biaya_upgrade(level):
    if level <=1:
        return 0
    return level*10 + biaya_upgrade(level-1)

#admin

def menu_admin():
    while True:
        bersihkan_layar()
        print("="*2, "Menu Admin", "="*2)
        print("1. Lihat item ")
        print("2. Hapus item")
        print("3. Tambah item")
        print("4. Logout")
        print("="*16)
        pil_admin = input_menu()

        if pil_admin =="1":
            bersihkan_layar()
            print("= Item yang ada =")
            list_katalog()
            tekan_enter()

        elif pil_admin == "2":
            bersihkan_layar()
            if jumlah_item_katalog() == 0:
                print("Katalog kosong")
                tekan_enter()
                continue

            print("= Item mana yang mau dihapus =")
            list_katalog()
            pil_hap = input_angka("\nPilihan (Enter untuk cancel):", 1, jumlah_item_katalog())
            if pil_hap is None:
                continue

            nama = list(katalog)[pil_hap - 1]
            katalog.pop(nama)
            print("\n", nama, "dihapus dari katalog")
            tekan_enter()

        elif pil_admin == "3":
            bersihkan_layar()
            print("= Tambahkan Item ke katalog =")
            nama = input("Nama item: ")
            base = input("Base level: ")

            try:
                base = int(base)
            except ValueError:
                print("\nBase level harus berupa angka")
            else:
                if nama == "":
                    print("\nInput tidak boleh kosong")
                elif base < 1 or base > max_level:
                    print("\nBase level harus 1-10")
                elif nama in katalog:
                    print("\nItem sudah ada di katalog")
                else:
                    katalog[nama] = base
                    print("\n", nama, "ditambahkan ke katalog")
            finally:
                tekan_enter()
    
        elif pil_admin == "4":
            bersihkan_layar()
            break

        else:
            print("\nPilihan tidak valid")
            tekan_enter()

# user

def menu_user(inv):
    while True:
        bersihkan_layar()
        print("="*2, "Inventory User", "="*2)
        print("1. Lihat/Add item ")
        print("2. Upgrade item")
        print("3. Buang item")
        print("4. Logout")
        print("="*20)
        pil_user = input_menu()

        if pil_user == "1":
            bersihkan_layar()
            print("= Inventory kamu =")
            inventory(inv)

            print("\n= Katalog =")
            if jumlah_item_katalog() == 0:
                print("Katalog kosong")
                tekan_enter()
                continue
            list_katalog()

            pilihan = input_angka("\nItem apa yang mau diambil? (Enter untuk kembali): ", 1, jumlah_item_katalog())

            if pilihan is None:
                continue

            nama = list(katalog)[pilihan - 1]
            if nama in inv:
                print("\n" + nama, "sudah ada di inventory")
            else:
                base = katalog[nama]
                inv[nama] = {"base": base, "level": base}
                print("\n" + nama, "masuk ke inventory")
            tekan_enter()

        elif pil_user == "2":
            bersihkan_layar()
            if len(inv) == 0:
                print("Inventory kosong")
                tekan_enter()
                continue

            print("= Item yang mau di-upgrade")
            for nomor, (nama, base) in enumerate(inv.items(), 1):
                sisa = biaya_upgrade(max_level) - biaya_upgrade(base["level"])
                print(nomor, ".", nama)
                print("     Level sekarang:", base["level"], "/", max_level)
                print("     Total biaya sampai max:", sisa)

            pil_up = input_angka("\nPilihan (Enter untuk cancel): ", 1, len(inv))
            if pil_up is None:
                continue

            nama = list(inv)[pil_up - 1]
            if inv[nama]["level"] >= max_level:
                print("\nLevel item sudah maksimal")
            else:
                inv[nama]["level"] += 1
                print("\n" + nama, "upgrade sukses")
            tekan_enter()

        elif pil_user =="3":
            bersihkan_layar()
            if len(inv) == 0:
                print("Inventory kosong")
                tekan_enter()
                continue

            print("= Item mana yang mau dibuang? =")
            inventory(inv)

            pil_buang = input_angka("\nPilihan (Enter untuk cancel): ", 1, len(inv))
            if pil_buang is None:
                continue

            nama = list(inv)[pil_buang - 1]
            inv.pop(nama)
            print("\n" + nama, "dibuang dari inventory")
            tekan_enter()
 
        elif pil_user == "4":
            bersihkan_layar()
            break
 
        else:
            print("\nPilihan tidak valid")
            tekan_enter()

def login():
    bersihkan_layar()
    print("=" * 3, "Login", "=" * 3)
    user = input("Username: ")
    pw = input("Password: ")
 
    akses = cek_login(user, pw)
 
    if akses == "":
        print("\nUsername atau Password salah")
        tekan_enter()
    elif akses == "admin":
        menu_admin()
    elif akses == "user":
        menu_user(akun[user]["inv"])

def register():
    bersihkan_layar()
    print("=" * 3, "Register", "=" * 3)
    user = input("User: ")
    pw = input("Password: ")
 
    if user == "" or pw == "":
        print("\nUsername dan password tidak boleh kosong!")
    elif user in akun:
        print("\nUsername sudah dipakai!")
    else:
        akun[user] = {"password": pw, "akses": "user", "inv": {}}
        print("\nRegistrasi berhasil! Silakan login.")
    tekan_enter()


def main():
    while True:
        bersihkan_layar()
        print("=" * 5, "Menu", "=" * 5)
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("=" * 16)
        pil_menu = input_menu()
 
        if pil_menu == "1":
            login()
        elif pil_menu == "2":
            register()
        elif pil_menu == "3":
            bersihkan_layar()
            print("Sampai jumpa!")
            break
        else:
            print("\nPilihan tidak valid!")
            tekan_enter()
 

if __name__ == "__main__":
    main()