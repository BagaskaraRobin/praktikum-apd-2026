from prettytable import PrettyTable
from tool import bersihkan_layar

def tampilan_menu():
    bersihkan_layar()
    tabel_menu = PrettyTable()
    tabel_menu.field_names = ["No.", "Menu Utama"]
    tabel_menu.align = "l"
    tabel_menu.add_row(["1", "Login"])
    tabel_menu.add_row(["2", "Register"])
    tabel_menu.add_row(["3", "Exit"])
    print(tabel_menu)

def tampilan_admin():
    bersihkan_layar()
    tabel_admin = PrettyTable()
    tabel_admin.field_names = ["No.", "Menu Admin"]
    tabel_admin.align = "l"
    tabel_admin.add_row(["1", "Lihat Katalog"])
    tabel_admin.add_row(["2", "Tambah Item"])
    tabel_admin.add_row(["3", "Hapus Item"])
    tabel_admin.add_row(["4", "Logout"])
    print(tabel_admin)

def tampilan_user():
    bersihkan_layar()
    tabel_user = PrettyTable()
    tabel_user.field_names = ["No.", "Menu User"]
    tabel_user.align = "l"
    tabel_user.add_row(["1", "Lihat Katalog"])
    tabel_user.add_row(["2", "Lihat Inventory"])
    tabel_user.add_row(["3", "Upgrade Item"])
    tabel_user.add_row(["4", "Logout"])
    print(tabel_user)