# ==========================================================
# Nama : Adrian Hermawan
# NIM : J0403251044
# Kelas : B1
# ==========================================================

# ========================================================== 
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
# ========================================================== 
 
class Node: 
    def __init__(self, no, nama, servis): 
        self.no = no 
        self.nama = nama 
        self.servis = servis 
        self.next = None 
 
 
class QueueBengkel: 
    def __init__(self): 
        self.front = None 
        self.rear = None 
 
    def enqueue(self, no, nama, servis): 
        # TODO: Tambahkan data ke antrian 

        #instintiansi node baru
        nodeBaru = Node(no, nama, servis)
        
        #jika data masih kosong, node baru jadi front sekaligus rear
        if self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru

        #geser pointer rear ke node baru    
        self.rear.next = nodeBaru
        self.rear = nodeBaru
 
    def dequeue(self): 
        # TODO: Layani pelanggan terdepan

        #taruh data pertama ke variabel
        layani = self.front

        #pindahkan pointer front ke data selanjutnya
        self.front = self.front.next
        
        print(f"Antrian nomor {layani.no}, {layani.nama} dengan paket servis {layani.servis} akan segera dikerjakan.")
 
    def tampilkan(self): 
        # TODO: Tampilkan seluruh antrian 
        
        #taruh self.front di current
        current = self.front
        
        #kalau queue kosong
        if self.front is None:
            print("Maaf, belum ada antrian terisi.")
            return
        
        
        nomor = 1
        
        #print sampai queue sampai none(data terakhir)
        while current is not None:
            print(f"{nomor}. {current.no} - {current.nama} - {current.servis}")
            current = current.next
            nomor +=1    
 
 
 
def main(): 
    q = QueueBengkel() 
 
    while True: 
        print("\n=== Sistem Antrian Bengkel ===") 
        print("1. Tambah Pelanggan") 
        print("2. Layani Pelanggan") 
        print("3. Lihat Antrian") 
        print("4. Keluar") 
 
        pilih = input("Pilih menu: ") 
 
        if pilih == "1": 
            no = input("No Antrian : ") 
            nama = input("Nama      : ") 
            servis = input("Servis    : ") 
            q.enqueue(no, nama, servis) 
 
        elif pilih == "2": 
            q.dequeue() 
 
        elif pilih == "3": 
            q.tampilkan() 
 
        elif pilih == "4":
            print("Program Selesai. Terima Kasih") 
            break 
 
        else: 
            print("Pilihan tidak valid")
            
main()