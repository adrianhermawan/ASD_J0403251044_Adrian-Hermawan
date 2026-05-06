#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 12 - Graph II: Shortest Path 
#====================================================

#====================================================
# Materi 2: Algoritma Bellman Ford
#====================================================

graph = {   #membuat graph
    'A':{'B':5, 'C':4}, 
    'C':{'B':-2}, 
    'B':{}
    
}

def bellman_ford(graph, start): 
    
    #jarak awal, jarak = infinite, belum diketahui
    distances = {node: float('inf') for node in graph} 

    #jarak node awal = 0
    distances[start] = 0 
 
    # Relaksasi berulang 
    #relaksasi dilakukan sebanyak (jumlah node-1) kali
    #karena jalur terpanjang maksimal melewati n-1 edge
    for _ in range(len(graph) - 1): 
        
        #loop untuk setiap node dalam graph
        for node in graph: 
            
            #loop untuk setiap tetangga
            for neighbor, weight in graph[node].items(): 
                
                #cek apakah jarak baru lebih kecil
                #jarak baru = jarak ke node sekarang + bobot edge
                if distances[node] + weight < distances[neighbor]: 
                    
                    #jika lebih kecil, update jarak
                    distances[neighbor] = distances[node] + weight 
 
    return distances 

hasil = bellman_ford(graph, 'A')
print(hasil)

# Dijkstra = cepat, pakai heap, tidak bisa bobot negatif
# Bellman-Ford = lambat, tanpa heap, bisa bobot negatif