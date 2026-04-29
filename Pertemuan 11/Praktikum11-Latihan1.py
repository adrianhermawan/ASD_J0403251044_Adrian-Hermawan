# ============================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B/P1
#=============================================

#=============================================
# Latihan 1: Studi Kasus BFS
#=============================================

from collections import deque
#library queue

#graph =  representasi hubungan antar lokasi
graph = {
    'Rumah':['Sekolah','Toko'], #dari rumah bisa ke sekolah & toko
    'Sekolah':['Perpustakaan'], #dari sekolah bisa ke perpustakaan
    'Toko':['Pasar'], #dari toko bisa ke pasar
    'Perpustakaan': [], #tidak ada jalur lanjutan
    'Pasar':[]
}

#fungsi bfs
def bfs(graph, start):
    visited=set() #menyimpan node yang sudah dikunjungi
    queue = deque([start]) #queue dimulai dari node awal

    visited.add(start) #tandai node awal sebagai visited

    while queue:
        node = queue.popleft() #ambil node paling depan (fifo)
        print(node, end=" ")

        #cek semua tetangga dari node sekarang
        for neighbor in graph[node]:
            if neighbor not in visited: #kalau neighbor belum dikunjungi
                visited.add(neighbor) #kunjungi
                queue.append(neighbor) #masukkan ke queue

print('BFS dari Rumah: ')
bfs(graph, 'Rumah')


#=========================================================
# 1. Node mana yang dikunjungi pertama?
# Node pertama yang dikunjungi adalah rumah, karena BFS selalu memulai dari node awal

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# BFS menjelajah graph per level
# Node yang paling dekat dikunjungi lebih dulu
# Menggunakan queue, berurutan dari yang terdekat

#3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Hasil BFS akan mengikuti struktur graph, karena BFS itu berdasarkan level