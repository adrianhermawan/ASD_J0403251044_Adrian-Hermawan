# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================================================
# Materi 1: Implementasi Kruskal
# ==================================================================

#daftar edge: (bobot, node1, node2)
edges = [
    (1,'C','D'),
    (2,'A','C'),
    (3, 'B','D'),
    (4,'A','B'),
    (5,'A','D')
]

#mengurutkan edge berdasarkan bobot
edges.sort()

mst = []
total_weight = 0

#set sederhana untuk node yang sudah dipilih
connected = set()

for weight, u, v in edges:

    #jika edge tidak membentuk cycle sederhana
    #kalau salah satu node belum pernah terhubung
    if u not in connected or v not in connected:

        #input edge ke mst
        mst.append((u,v,weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree: ")

for edge in mst:
    print(edge)

print('Total bobot =', total_weight)

#alur
#1. urutkan edge dengan bobot terkecil
#2. cek apakah edge membentuk cycle atau tidak, dengan cara:
# cek kedua node apakah sudah ada di set connected
# kalau keduanya ada di set connected berarti membentuk cycle
# kalau tidak ada atau hanya salah satu, tidak membentuk cycle
#3. masukkan edge ke mst
#4. ulang dari nomor 2
