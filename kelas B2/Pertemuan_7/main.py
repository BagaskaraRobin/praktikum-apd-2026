# # # # # def sapa():
# # # # #     print("hi")

# # # # def persegi(sisi):
# # # #     hasil = sisi*sisi
# # # #     return hasil

# # # # persegi(5)

# # # def sapa(nama="migeul"):
# # #     return f"Hi {nama}"

# # # print(sapa())

# # def menu():
# #     print("1. Create")
# #     print("2. Read")
# #     print("3. Update")
# #     print("4. Delete")

# #     pilihan = input("Pilihan: ")

# nama = "Larry"
# prodi = "Informatika"

# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# def sapa ():
#     return "hi"

# print (sapa())

def faktorial(n):
#Base Case: Kondisi fungsi berhenti

    if n == 0 or n == 1:
        return 1
    
#Rekursive Case: Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)
    
#Memanggil fungsi
hasil_faktorial = faktorial(4)
print(f"Hasil dari 4! {hasil_faktorial}")