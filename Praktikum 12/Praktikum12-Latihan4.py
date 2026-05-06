#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 12 - Graph II: Shortest Path 
#====================================================

#====================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
#====================================================

import heapq 
# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
'Perpustakaan': {'Lab': 3}, 
'Kantin': {'Lab': 4, 'Aula': 7}, 
'Lab': {'Aula': 1}, 
'Aula': {} 
} 
def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    priority_queue = [(0, start)] 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        if current_distance > distances[current_node]: 
            continue 
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 

hasil = dijkstra(graph, 'Gerbang') 
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit") 

# Jawaban Analisis: 
# 1. Lokasi mana yang paling dekat dari Gerbang? 
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# 1. Kantin, berjarak 2 menit
# 2. Waktu tercepat dari gerbang ke aula adalah 7 menit
# 3. Tidak, tergantung bobotnya, misal saja Kantin ke aula
# Kantin ke aula melalui lab hanya berjarak 5 menit
# sedangkan kalau kantin langsung ke aula berjarak 7 menit
# 4. Karena semua bobot bernilai positif,
# sehingga Dijkstra dapat menghitung jarak terpendek dengan cepat dan akurat