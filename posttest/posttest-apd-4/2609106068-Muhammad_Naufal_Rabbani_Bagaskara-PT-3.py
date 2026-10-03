#Program Login

nama = "robin"
nim = "68"

percobaan = 0

while percobaan < 3:
    username = input("Masukkan username: ").lower().strip()
    password = input("Masukkan password: ").lower().strip()

    if username == nama and password == nim:
        print("Login berhasil, selamat datang", nama)
        break
    elif username != nama and password != nim:
        print("Username dan Password salah")
    elif username != nama:
        print("Username  salah")
    else:
        print("Password salah")
        
    percobaan += 1

    if percobaan == 3:
        print("Anda telah mencoba login 3 kali. Silakan coba lagi nanti.")
        exit()
    else:
        print("Silakan coba lagi. Sisa percobaan:", 3 - percobaan)

# Program distribusi paket

while True:
    menu = input('''
====Welcome to Los Pollos Hermanos! What would you like to order?===

1. Paket Reguler  : 1 porsi makanan
2. Paket Anak     : 1 porsi makanan
3. Paket Keluarga : 4 porsi makanan

Exit program? Input 4 to exit.
====================================================================
Input your choice (1-4):''')

    if not menu.isdigit() or not 1 <= int(menu) <= 4:
        print("Invalid option. Please choose a valid menu option.")
        continue

    menu = int(menu)

    if menu == 4:
        print("Thank you for visiting Los Pollos Hermanos. Goodbye!")
        exit()

    while True:
        jumlah = input("How many packages would you like to order?: ")
        if not jumlah.isdigit() or not 1 <= int(jumlah):
            print("Silahkan masukan angka dan angka lebih dari 0")
            continue
        jumlah = int(jumlah)
        break

# Perogram hasil

    if menu == 3:
        porsi = 4
    else:
        porsi = 1

    total_porsi = 0

    for i in range(jumlah):
        total_porsi += porsi
        if total_porsi >= 20:
            bonus = "5 paket buah"
        elif total_porsi >= 10 and total_porsi < 20:
            bonus = "3 botol susu"
        elif total_porsi >= 5 and total_porsi < 10:
            bonus = "1 paket vitamin"
        else:
            bonus = "Tidak ada bonus"

    if menu == 1:
        jenis_paket = "Paket Reguler"
    elif menu == 2:
        jenis_paket = "Paket Anak"
    elif menu == 3:
        jenis_paket = "Paket Keluarga"

    print("======Order Summary======")
    print("Jenis Paket:      ", jenis_paket)
    print("Jumlah Paket:     ", jumlah)
    print("Total Porsi:      ", total_porsi, "porsi")
    print("Penerima Manfaat: ", total_porsi,"orang")
    print("Bonus:            ", bonus)
    print("=========================")
    break