#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# Praktikum 12 - Graph II: Shortest Path 
#====================================================

#====================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
#====================================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 

# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D 
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 


# Jawaban Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# 2. Berapa total bobot jalur A -> C -> D? 
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

# 1. Total bobot jalur A -> B -> D adalah 9,
# A -> B = 4, B -> D = 5, jadi totalnya 9

# 2. Total bobot jalur A -> C -> D adalah 3,
# A -> C = 2, C -> D = 1, jadi totalnya 3

# 3. Jalur A -> C -> D, karena bobotnya lebih kecil dari A -> B -> D
# yaitu 3 < 9

# 4. Karena jalur terpendek ditentukan oleh bobot edge nya
# tidak terpengaruh banyaknya edge
# bisa saja edge hanya 1 tapi bobot 100