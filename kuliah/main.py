id = {"nama":"Robin", "NIM":68, "Prodi":"informatika", "semester":1}
id.update({"alamat":"Jl, AWS", "email":"bagaskararobin@gmail.com"})

for i, j in id.items():
    print(i, ":", j)

jumlah_item = len(id)
print("\nJumlah item:", jumlah_item)

id.update({"semester": 2})

hapus_item = id.pop("alamat")
for i, j in id.items():
    print(i, ":", j)
