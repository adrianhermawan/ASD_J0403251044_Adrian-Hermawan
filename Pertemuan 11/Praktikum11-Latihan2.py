# ============================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B/P1
#=============================================

#=============================================
# Latihan 2: Studi Kasus BFS (Eksplorasi Jalur)
#=============================================

from collections import deque
#library queue

#graph =  representasi hubungan antar lokasi
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D': [], 
    'E':[],
    'F':[]
}

#fungsi bfs
def bfs(graph, start,visited):
    visited.add(node)

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

visited = set()

print('BFS dari A: ')
bfs(graph, 'A', visited)


#=========================================================
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# DFS menggunakan konsep rekursi atau stack, sehingga selalu
# melanjutkan ke satu cabang sampai paling dalam sebelum kembali (backtracking)
# karena itu, DFS akan mengunjungi node terdalam terlebih dahulu.

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Urutan hasil DFS akan berubah.
# Contoh: jika 'A' : ['C', 'B'], maka DFS akan ke C dulu baru ke B
# Jadi urutan traversal sangat bergantung pada urutan list neighbor

# 3. Bandingan hasil DFS dengan BFS pada graph yang sama
# DFS (Depth First Search):
# A B D E C F -> Masuk ke dalam dulu baru pindah cabang

# BFS (Breadth First Search):
# A B C D E F -> per level (meleber dulu)

# Perbedaan utamanya adalah,
# DFS menelusuri sedalam mungkin (depth) sedangkan
# BFS menelusuri per tingkat (breadth)