#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 12 - Graph II: Shortest Path 
#====================================================

#====================================================
# Latihan 2: Implementasi Dijkstra 
#====================================================

import heapq 
# Weighted graph dengan bobot positif 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """ 

    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]

    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    return distances 
 
 
hasil = dijkstra(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 
# 2. Berapa jarak terpendek dari A ke C? 
# 3. Berapa jarak terpendek dari A ke D? 
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 

# 1. Jarak terpendek dari A ke B adalah 4
# 2. Jarak terpendek dari A ke C adalah 2
# 3. Jarak terpendek dari A ke D adalah 3
# 4. Karena bobot dari A ke B saja sudah 4, ditambah B ke D berbobot 5
# menjadikan totalnya 9, sedangkan A ke C hanya 2, dan C ke D hanya berbobot 1
# lebih dekat melalui C

# 5. Memilih node dengan jarak terkecil secara otomatis
# (jarak terkecil, node)
# contoh: pq = [(2, 'C'), (4, 'B')]
# yang diambil C dulu
#priority queue mengambil langsung jarak terkecil tanpa cek semua node
# pq menyimpan node yang akan diproses

# 6. Karena Dijkstra, setiap langkahnya akan langsung mengambil jarak yang terpendek
# tanpa cek jalur lainnya, padahal dengan bobot negatif masih bisa ditemukan jalur yang
# lebih pendek di langkah selanjutnya

#misal:
# A -> B : 3
# B -> D : 1
# A -> C : 5
# C -> D : -5
# Dijkstra akan mendapatkan hasil jarak terpendek A ke D melalui B
# Karna pada langkah pertama ia akan memilih B tanpa cek langkah ke C selanjutnya