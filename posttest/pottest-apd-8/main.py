
from tool import bersihkan_layar, tekan_enter, input_menu, jumlah_item_katalog, input_angka, list_katalog, inventory, biaya_upgrade, list_katalog
from data import katalog, max_level
from auth import login
from register import register
from menu import tampilan_admin, tampilan_user, tampilan_menu


def menu_admin():
    while True:
        bersihkan_layar()
        tampilan_admin()
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

def menu_user(inv):
    while True:
        bersihkan_layar()
        tampilan_user()
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


def main():
    while True:
        bersihkan_layar()
        tampilan_menu()
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