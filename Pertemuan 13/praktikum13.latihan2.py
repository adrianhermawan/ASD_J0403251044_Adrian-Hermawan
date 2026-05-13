# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 
# Latihan 2: Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 
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

# Jawaban Analisis: 
# 1. Edge mana yang dipilih pertama kali? 
# Edge C-D dengan bobot 1

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Karena tujuan algoritma kruskal adalah membuat Minimum Spanning Tree
# Yaitu spanning tree dengan total bobot sekecil mungkin
# Jadi edge dengan bobot terkecil dipilih dahulu agar total akhirnya minimum 
# 
# 3. Berapa total bobot MST yang dihasilkan? 
# 6
# C-D=1, A-C=2, B-D=3, 1+2+3 = 6

# 4. Mengapa edge tertentu tidak dipilih?
# Karena bobotnya besar dan sudah bisa diwakilkan dengan edge yang bobot totalnya lebih kecil
# Misal:
# edge A-D tidak terpilih karena bobotnya 5
# edge ini sudah terwakilkan oleh edge A-C, C-D dengan bobot 3
 