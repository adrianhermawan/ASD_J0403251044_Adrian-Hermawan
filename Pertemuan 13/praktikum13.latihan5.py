# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 
# Latihan 5: Tugas Mandiri: Buat Program MST dengan Kasus Baru 
# Kasus 1. Jaringan jalan antarkota
# ========================================================== 

import heapq

graph = {
    'Bogor': {'Jakarta':5, 'Depok':2},
    'Depok': {'Bogor':2, 'Jakarta':3, 'Bandung':4},
    'Jakarta': {'Bogor':5, 'Depok':3, 'Bandung':6},
    'Bandung': {'Depok':4, 'Jakarta':6}
}

def prim(graph, start):

    #node awal masuk visited
    visited = set([start])

    edges = []

    #masukin edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight,start,neighbor))

    #menyiapkan mst dan total weight
    mst = []
    total_weight = 0

    #loop  utama
    while edges:

        #heappop otomatis mengambil bobot terkecil
        weight, u, v = heapq.heappop(edges)

        #cek apakah node tujuan sudah dikunjungi
        if v not in visited:
            #kalau belum:

            #node tandai visited
            visited.add(v)

            #tambahkan edge ke mst dan total weight
            mst.append((u,v,weight))
            total_weight += weight

            #tambahkan edge baru dari node v (awal kan A, berarti sekarang C)
            for neighbor, w in graph[v].items():

                #kalau neighbor belum dikunjungi, masukkan ke heap edges
                if neighbor not in visited:
                    heapq.heappush(edges, (w,v,neighbor))

    return mst, total_weight

mst, total = prim(graph, 'Bogor')

print('Minimum Spanning Tree: ')

for edge in mst:
    print(edge)

print('Total Bobot minimum: ',total)

# Jawaban Analisis: 
# 1. Kasus apa yang dipilih?
# Kasus 1, Jaringan jalan antarkota

# 2. Algoritma apa yang digunakan? 
# Program ini menggunakan algoritma Prim

# 3. Edge mana saja yang dipilih dalam MST? 
# edge Bogor-Depok bobot 2
# Depok-Jakarta bobot 3
# Depok-Bandung bobot 4

# 4. Berapa total bobot MST?
# Bobot totalnya ada 9
 
# 5. Mengapa edge tertentu tidak dipilih?
# Edge Bogor–Jakarta (5) tidak dipilih karena sudah ada jalur yang lebih murah
# Bogor–Depok (2)
# Depok–Jakarta (3)

# Edge Jakarta–Bandung (6) juga tidak dipilih karena ada edge yang lebih kecil, yaitu:
# Depok–Bandung (4) 