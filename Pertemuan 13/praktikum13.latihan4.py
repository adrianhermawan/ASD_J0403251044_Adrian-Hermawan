# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 
# Latihan 4: Studi Kasus: Jaringan Kabel Antar Gedung
# ========================================================== 

#daftar edge: (bobot, node1, node2)
edges = [
    (4,'GedungA','GedungB'),
    (2,'GedungA','GedungC'),
    (3, 'GedungB','GedungD'),
    (1,'GedungC','GedungD'),
    (5,'GedungA','GedungD')
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

print('Total biaya minimum =', total_weight)

# Jawaban Analisis: 
# 1. Algoritma apa yang digunakan? 
# Algoritma Kruskal

# 2. Edge mana saja yang dipilih?
# Edge gedung C-D, A-C, B-D 

# 3. Berapa total biaya minimum?
# Total biaya minimumnya 6 
 
# 4. Mengapa MST cocok digunakan pada kasus ini?
# Karena MST dapat mencari jalur untuk seluruh node yang paling efisien, cocok untuk mencari jalur kabel internet antar gedung
# untuk meminimalkan cost dan biaya maintenance
# MST membuang jalur yang tidak perlu 