# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================================================
# Materi 2: Implementasi Prim
# ==================================================================

import heapq

graph = {
    'A': {'B':4, 'C':2, 'D':5},
    'B': {'A':4,'D':3},
    'C': {'A':2,'D':1},
    'D': {'A':5,'B':3,'C':1}
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

mst, total = prim(graph, 'A')

print('Minimum Spanning Tree: ')

for edge in mst:
    print(edge)

print('Total Bobot: ',total)

# iterasi
# visited = A
# heap = 2AC, 4AB, 5AD
# AMBIL TERKECIL = 2AC
#TAMBAHKAN EDGE C
# VISITED = A C
# HEAP = 1CD, 4AB, 5AD

# JADI HEAP EDGES SEBELUMNYA TETAP ADA DAN TETAP DIBANDINGKAN DENGAN EDGES DARI NODE TERBARU