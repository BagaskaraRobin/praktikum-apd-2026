# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

# print(formula1[0])

# for index,elemen in enumerate (formula1, start=1):
#     print(index, elemen)

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit.append("Spa-Francorchamps")
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay', 'Spa-Francorchamps']

# sirkuit.extend(["Larry", "Rendy"])
# print(sirkuit)

# sirkuit.insert(2, "Alfi")
# print(sirkuit)

# sirkuit[3] = "Apip" 
# print(sirkuit)

# sirkuit[0:1] = ["Rizky", "Naufal"]
# print(sirkuit)

# sirkuit[0:5:2] = ("Rizky", "Naufal", "opung")
# print(sirkuit)

# del sirkuit[4]
# print(sirkuit)

# sirkuit.remove("Rizky")
# print(sirkuit)

# nama_hapus = sirkuit.pop(1)
# print(sirkuit)
# print(nama_hapus)

# print(sirkuit[0:4:2])

# matkul1 = ["APD", "Kalkulus", "agama"]
# matkul2 = ["do", "re", "mi"]

# gabung = matkul1 + matkul2
# print(gabung)

# angka1 = [1,2,3]
# angka2 = [4,5,6]

# agabung = angka1 + angka2
# print(agabung)

# matkul2 = matkul2 * 3
# print(matkul2)

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]

# print(line_up[2][1])

# for i in line_up:
#     for j in i:
#         print(j)

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))

data = ("rafi")

print

listchara = list(chara)
print(type(listchara))

listchara.append("naruto")
print(listchara)

del listchara [6]
print(listchara)

chara = ("Yukari", "Yukino", "Odette", "Senku")
(Persona, Oregairu, Genshin, DrStone) = chara

print(Persona)
print(Oregairu)

