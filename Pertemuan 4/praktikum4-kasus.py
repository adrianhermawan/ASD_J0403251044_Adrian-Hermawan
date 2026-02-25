#====================================================
#Nama: Adrian Hermawan
#NIM: J0403251044
#Kelas: B1
#====================================================

#====================================================
#Studi Kasus: Sistem Antrian Layanan Akademik
#Implementasi Queue
#Enqueue : memindahkan pointer rear
#Dequeue : memindahkan pointer front
#Queue ==> Front -> A -> B -> C -> Rear
#Front dilayani dahulu, rear tempat masuk data baru
#Deque A duluan
#====================================================

#mendefinisikan Node (Unit dasar linked list)
class node:
    def __init__(self, nim, nama):
        self.nim =nim #Menyimpan NIM mahasiswa
        self.nama =nama #Menyimpan nama mahasiswa
        self.next =None #pointer ke next node

#mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None    

    #menambahkan data baru ke bagian rear, antrian mahasiswa yang mengajukan layanan akademik
    def enqueue(self,nim,nama):
        Nodebaru = node(nim,nama)
        
        #kalau data masih kosong, data baru akan jadi front sekaligus rear
        if self.front is None:
            self.front = Nodebaru
            self.rear = Nodebaru
            return
        
        #input data dan pindah pointer
        self.rear.next = Nodebaru
        self.rear = Nodebaru

    #menghapus data paling depan
    def dequeue(self):
        if self.front is None:
            print("Antrian Kosong. Tidak ada Mahasiswa yang dilayani")
            return None

        #simpan daaaaata front di node dilayani
        node_dilayani = self.front
        
        #geser pointttter ke next front
        self.front = self.front.next
        
        #jika front menjadi none(data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None


        return node_dilayani
        
    def tampilkan(self):
        



        print("Daftar Antrian Mahasiswa (Front -> Rear)")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no +=1


#program utama

def main():
    

    #instantiansi
    q = queueAkademik()

    while True:
        print("======== Sistem Antrian Akademik ========")
        print("1. Tambah Antrian Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")
        
        elif pilihan == "3":
            q.tampilkan()
        
        elif pilihan =="4":
            print("Program Selesai. Terima Kasih")
            break
        
        else:
            print("Pilihan tidak valid. Silahkan coba lagi")
main()
