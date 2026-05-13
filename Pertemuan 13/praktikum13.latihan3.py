# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 
# Latihan 3: Implementasi Sederhana Algoritma Prim 
# ========================================================== 

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

# Jawaban Analisis: 
# 1. Node awal apa yang digunakan? 
# mst, total = prim(graph, 'A') => node awal yang digunakan adalah A

# 2. Edge mana yang dipilih pertama kali? 
# edge A-C dengan bobot 2
# edge terkecil dibanding dengan
# A-B=4, A-D=5

# 3. Bagaimana Prim menentukan edge berikutnya?
# di prim ada variabel edges, misal pertama dari node A, edge nya akan masuk ke variabel edges
# dan tetap akan ada disana, jadi saat lanjut ke node selanjutnya, misal node C,
# edge dari node A tetap dibandingkan dengan edge dari node C, tetap dipilih yang paling kecil

# 4. Berapa total bobot MST yang dihasilkan?
# Total bobot = 6 
 
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Prim mengumpulkan seluruh edge beserta bobotnya, dan diurutkan dari yang terkecil
# Kalau kruskal membandingkan edgenya mulai dari node ke node, tidak sekaligus