nama_file = "data_barang.txt"


#untuk bikin dictionary dari data
def baca_data_barang(nama_file):
    dict_barang = {}
    
    #untuk mengambil data di file
    with open("stok_barang.txt","r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            
            #pisahin data
            parts = baris.split(",")
            kode,nama,stok_str = parts
            stok_int = int(stok_str)
            
            #masukin data ke dictionary
            dict_barang[kode] = {
            "nama" : nama,
            "stok" : stok_int    
            }
            
    return dict_barang

#buka_data = baca_data_barang(nama_file)
#print(baca_data_barang(nama_file))

#untuk menampilkan data yang tadi udah dibikin dictionary
def tampilkan_data(dict_barang):
    if len==0:
        print("Data tidak ditemukan")
        return
    
    #bikin header
    print("\n==================DATA STOK BARANG==================")
    print(f"{'KODE BARANG':<15} | {'NAMA BARANG':<20} | {'STOK BARANG':>10}")
    print("-"*52)

    #pindahin data ke variabel dan di print    
    for kode in sorted(dict_barang.keys()):
        nama = dict_barang[kode]["nama"]
        stok = dict_barang[kode]["stok"]
        print(f"{kode:<15} | {nama:<20} | {stok:>10}")

#print(tampilkan_data(baca_data_barang(nama_file)))

def cari_data(dict_barang):
    kode_input = input("Masukkan kode barang yang mau dicari:")
    
    #cari apakah kode yg diinput ada di dalam dictionary
    if kode_input in dict_barang:
        nama = dict_barang[kode_input]["nama"]
        stok = dict_barang[kode_input]["stok"]
        
        print("\n========DATA DITEMUKAN========")
        print(f"Kode: {kode_input}")
        print(f"Nama Barang: {nama}")
        print(f"Jumlah Stok: {stok}")
    else: print("\nData tidak ditemukan")

#print(cari_data(buka_data))

def update_nilai(dict_barang):
    kode = input("Masukkan kode barang yang mau diubah: ")
    
    #cek apakah barang ada di dictionary
    if kode not in dict_barang:
        print("\nBarang tidak ditemukan")
        return
    
    try: stok_baru = input("Masukkan jumlah stok terbaru:")
    except ValueError: #cek apakah inputnya angka atau bukan
        print("Stok harus berupa angka. Coba lagi")
        return
    
    stok_lama = dict_barang[kode]["stok"]
    dict_barang[kode]["stok"] = stok_baru
    print(f"Selamat, stok berhasil diperbarui dari {stok_lama} menjadi {stok_baru}")

#update_nilai(buka_data)

def simpan_data(nama_file, dict_barang):
    #buka file txt untuk di write
    with open("stok_barang.txt","w",encoding="utf-8") as file:
        for kode in sorted(dict_barang.keys()):
            nama = dict_barang[kode]["nama"]
            stok = dict_barang[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")
            
def tambah_data(dict_barang):
    
    kode = input("Masukkan kode barang dengan format(BRG0XX): ")
    #cek kode apakah panjangnya sesuai
    if len(kode)!=6:
        print("Masukkan kode yang valid")
        return
    
    #input nama dan stok
    nama = input("Masukkan nama barang: ")
    stok = input("Masukkan stok barang yang tersedia: ")
    
    #masukin inputan tadi ke dictionary
    dict_barang[kode]={
    "nama" : nama,
    "stok" : stok    
    }



def main():
    
     #menjalankan fungsi 1 load data
    buka_data = baca_data_barang(nama_file)
    tampilkan_data(buka_data)
    
    while True:
        print("\n====== MENU DATA STOK BARANG ======")
        print("1.Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan file")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            tambah_data(buka_data)

        elif pilihan == "4":
            update_nilai(buka_data)
    
        elif pilihan == "5":
            simpan_data(nama_file,buka_data)
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program Selesai")
            break

        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()