# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Latihan 1. Memahami Kode Program (Insertion Sort)
# ================================== 
 
def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data

# 1. Mengapa perulangan dimulai dari indeks 1? 
# Karena perulangannya berisi pembandingan key dengan data j, 
# sedangkan kalau dimulai dari indeks 0, tidak ada data j yang bisa dibandingkan dengan key
# jadi harus dimulai dari indeks 1, agar indeks ke 0 bisa langsung menjadi data j

# 2. Apa fungsi variabel key? 
# untuk menyimpan data yang akan dibandingkan dengan data kiri(sorted) sebelum disisipkan

# 3. Mengapa digunakan while, bukan for? 
# karena jumlah langkah pergeserannya tidak pasti di setiap iterasi

# 4. Operasi apa yang terjadi di dalam while? 
#operasi pembandingan key dengan data sebelah kiri
# while j >= 0 and data[j] > key:  (looping selama key lebih kecil dari data j)(perbandingan)
    #data[j + 1] = data[j]  #geser data j ke kanan (misal data[j] = 8, [3,8,5] => [3,8,8])
    #j -= 1 #lanjut perbandingan ke sebelah kiri


p = [90,12,142,72,856,21,100]

print("Hasil Sorting: ",insertion_sort(p))
    