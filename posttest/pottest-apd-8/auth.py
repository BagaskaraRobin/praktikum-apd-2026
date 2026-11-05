
from tool import bersihkan_layar, tekan_enter, cek_login
from data import akun


def login():
    from main import menu_admin, menu_user
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