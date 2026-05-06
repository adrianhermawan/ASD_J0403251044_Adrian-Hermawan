#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 12 - Graph II: Shortest Path 
#====================================================

#====================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path 
#====================================================

import heapq

graph = { 
'Bogor': {'Jakarta': 5, 'Depok': 2}, 
'Depok': {'Jakarta': 2, 'Bandung': 6}, 
'Jakarta': {'Bandung': 7}, 
'Bandung': {} 
} 

def dijkstra(graph, start):

    #distance awal tidak diketahui, atau infinite
    distances = {node: float('inf') for node in graph}
    
    #jarak node awal = 0
    distances[start] = 0

    # pq untuk ambil jarak terkecil
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        #skip jika sudah ada jarak yang lebih kecil
        if current_distance > distances[current_node]:
            continue

        # cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            #relaksasi (update jika lebih kecil)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

hasil = dijkstra(graph, 'Bogor') 
print("Jarak terpendek dari Bogor:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "Jam") 


# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang anda buat.

# 1. Bogor
# 2. Depok dengan jarak 2 dari Bogor
# 3. Bandung melalui Jakarta dengan jarak 12
# 4. Dijkstra bekerja dengan memilih node dengan jarak paling kecil dari node awal
# lalu memperbarui jarak ke tetangganya
# Proses ini diulang sampai semua node mendapat jarak terpendek.
