#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 12 - Graph II: Shortest Path 
#====================================================

#====================================================
# Materi 1: Algoritma Dijkstra
#====================================================

#untuk priority queue
import heapq

graph = {   #membuat graph
    'A':{'B':4, 'C':2}, #A -> B bobot 4, A->C bobot 2
    'B':{'D':5}, #B->D bobot 5
    'C':{'D':1}, #C->D bobot 1
    'D':{}
}

def dijkstra(graph,start): #fungsi dijkstra

    #menyimpan jarak minimum
    distances = {node:float('inf') for node in graph} #inisialisasi jarak
    #inisialisasi jarak
    #semua node set ke infinite
    #arti: belum diketahui jaraknya

    #jarak node awal = 0
    distances[start] = 0

    #priority queue
    pq = [(0, start)]

    while pq:
        #ambil node terdekat, misal (0, 'A')
        current_distance, current_node = heapq.heappop(pq)

        #periksa semua tetangga, tettangga A = B(4) dan C(2)
        for neighbor, weight in graph[current_node].items():

            #hitung jarak dari start ke tetangga, misal A ke B, 0 + 4 = 4
            distance = current_distance + weight

            #jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                #update jarak
                distances[neighbor] = distance

                #masukkan ke priority queue untuk diproses lagi
                heapq.heappush(pq, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')
print(hasil)

#output : {'A': 0, 'B': 4, 'C': 2, 'D': 3}
#maksudnya
#A ke A : 0
#A ke B : 4
#A ke C : 2
#A ke D : 3

# 1. Set semua jarak = ∞, start = 0
# 2. Masukkan start ke priority queue
# 3. Ambil node dengan jarak terkecil
# 4. Cek semua tetangga
# 5. Update jarak jika lebih kecil
# 6. Masukkan ke queue
# 7. Ulangi sampai queue kosong
# 8. Hasil = jarak terpendek dari start ke semua node