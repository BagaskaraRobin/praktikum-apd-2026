# # kartu = {"merah", "biru", "hijau"}

# # kartu.discard("hijau")

# # print(kartu)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}

# gabung = aslab1.union(aslab2)
# print(gabung)

# Matkul = {
#     "Matkul_ganjil" : "kalkulus",
#     "Matkul_genap" : "statistik"
# }

# print(Matkul(.get("Matukul_genap", "Key tidak ada")))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# # for i in game:
# #     print(i)
# # for i in game.keys():
# #     print(i)
# # for i in game.values():
# #     print(i)
# # for i, j in game.items():
# #     print(i, j)

# # game["resident evil"] = "horror"

# game.update({"resident evil" : "horror"})
# print(game)

# for i, j in game.items():
#     print(i, j)

# setdefault

# dict.fromkeys

menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
for kategori in j:
    print(kategori)
print("")