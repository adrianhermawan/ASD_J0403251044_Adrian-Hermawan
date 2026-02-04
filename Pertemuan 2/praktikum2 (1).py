nama_file = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {}

    #mengambil data
    with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
        for baris in file:
            baris=baris.strip()

            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim,nama,nilai_str=parts
            nilai_int = int(nilai_str)
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {
                "nama" : nama,
                "nilai" : nilai_int
            }
    return data_dict

#buka_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca:",len(buka_data))




#latihan 2: membuat fungsi menampilkan data
def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
    #Header
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}") 
    print("-" *32)

    '''
    untuk tampilan yang lebih rapi, atur f-string formating
    'NIM':<10 artinya:
    tampilkan nim <= rata kiri dengan lebar 10 karakter
    {'Nama':<12}
    Tampilkan nama rata kiri, dengan lebar kolom 12 karakter
    {'Nilai':>5}
    tampi;lan nilai rata kanan, dengan lebar kolom 5 karakter
    '''

    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama: <12} | {nilai:>5}")

#tampilkan_data(buka_data)

#latihan 3 mencari data

def cari_data(data_dict):
    nim_cari=input("Masukkan NIM yang ingin dicari:").strip()

    if nim_cari in data_dict:
        nama=data_dict[nim_cari]["nama"]
        nilai=data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM    : {nim_cari}")
        print(f"Nama   :{nama}")
        print(f"Nilai  :{nilai}")
    else:
        print('\nData tidak ditemukan')

#cari_data(buka_data)

#Latihan 4:update nilai

def update_nilai(data_dict):
    nim = input("Masukkan NIM mahasiswa yang mau diubah : ")

    if nim not in data_dict:
        print("Maaf, NIM tidak ditemukan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru(0-100) : "))
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru<0 or nilai_baru>100:
        print("Masukkan input nilai yang benar(0-100) : ")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    print(F"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)


#Latihan 5: simpan data

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buka_data)
#print("Data Berhasil Disimpan")

#latihan 6:menu
def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)
    
    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1.Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            update_nilai(buka_data)
    
        elif pilihan == "4":
            simpan_data(nama_file,buka_data)
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program Selesai")
            break

        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()