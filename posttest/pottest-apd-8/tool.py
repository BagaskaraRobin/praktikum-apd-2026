import os
from data import katalog, akun

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
            angka = int(teks)
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