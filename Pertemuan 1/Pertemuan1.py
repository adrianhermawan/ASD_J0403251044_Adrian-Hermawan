#Pertemuan 1, Data Structure & Algorithm

#Membuka file dengan mode read "r"
with open("data_mahasiswa.txt", "r", encoding="utf=8") as file:
    isi_file = file.read()
print(isi_file)

print("==Hasil Read==")
print("Tipe Data: ", type(isi_file))
print("Jumlah Karakter: ", len(isi_file))
print("Jumlah Baris: ", isi_file.count("\n")+1)

#Membuka file per baris
print("\n\n==Membaca File per Baris==")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris  = baris.strip
        print("Baris ke-", jumlah_baris)
        print("isinya: ", baris)

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
print("\n\n")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print(f"NIM : {nim} | NAMA : {nama} | NILAI : {nilai}")

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan menyimpan ke List

data_list = [] #list kosong utk menampung data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim1, nama1, nilai1 = baris.split(",")

        #simpan sebagai list
        data_list.append([nim1,nama1,int(nilai1)])

print("\n==Data Mahasiswa DALAM LIST==")
print(data_list)

print("\n==Jumlah Record DALAM LIST==")
print("Jumlah Record", len(data_list))

print("\n==Menampilkan Data Record Tertentu==")
print("Contoh Record Pertama: ", data_list[0])

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca file dan menyimpan ke dictionary

data_dict = {} #dic kosong utk menyimpan nilai
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim2, nama2, nilai2 = baris.split(",")
        
        #simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim2] = {       #key
            "nama": nama2,         #value
            "nilai": int(nilai2)  #value
        }

print("\n==Data Mahasiswa Dalam Dictionary==")
print(data_dict)