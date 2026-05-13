# ==================================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 13 - Graph III: Spanning Tree
# ==================================================================
# Latihan 1: Memahami konsep spanning tree
# ==================================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E')
]

#contoh spanning tree
spanning_tree = [
    ('A', 'B'),
    ('B', 'D'),
    ('D', 'E'),
    ('A', 'C')
]
#tidak ada yang membentuk cycle

print('Edge pada graph: ')
for edge in edges:
    print(edge)

print("\nSpanning Tree")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("\nJumlah edge spanning tree =", len(spanning_tree))

# JAWABAN ANALISIS
# 1. APA PERBEDAAN GRAPH AWAL DAN SPANNING TREE?
# GRAPH AWAL MEMBENTUK CYCLE SEDANGKAN SPANNING TREE TIDAK
# spanning tree adalah bagian dari graph awal itu sendiri
# spanning tree adalah jalur paling efisien untuk mencapai seluruh node yang ada di node awal

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Karena tujuan spanning tree adalah menghubungkan semua node dengan jalur paling efisien
# Kalau ada cycle berarti jalurnya tidak lagi efisien karena ada node yang terhubung secara double

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Karena spanning tree hanya mengambil edge yang benar benar diperlukan untuk menghubungkan semua node
# Edge yang tidak perlu tidak akan diambil
