from tool import bersihkan_layar, tekan_enter
from data import akun

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