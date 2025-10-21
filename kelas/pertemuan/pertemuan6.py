# buah = {"apel", "jeruk", "mangga", "apel"}
# buah = ([“apel”, “jeruk”, “mangga”, “apel”])
# print(buah)



# daftar_buku = {
#     "Buku 1" : "Bumi Manusia"
#     "Buku 2" : "Laut Bercerita"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"
# }
# }
# # print(Biodata)
# # for i, j  in Biodata.items():
# #     print(i)
# #     print(j) #valuenya

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama")")


# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})  #klo key yg diupdate sama aja kaya nambah
# #Setelah Ditambah
# print(Film)
# #Sebelum Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'}
# #Setelah Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours':
# 'Thriller'}

# del Film['The Conjuring']
# print(Film)
# Film.clear()
# print(Film)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0]) #here we go again


#set kosong angka = set()
# a = {10, 11, 12}
# b = {11, 13, 14}
# c = a | b
# print(c)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}

print("Nilai : ", Nilai.setdefault("Kimia", 70))