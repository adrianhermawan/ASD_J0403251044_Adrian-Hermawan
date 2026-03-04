# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Latihan 2. Melengkapi Potongan Kode
# ================================== 


#1. Lengkapi kondisi agar menjadi sorting ascending.
def insertion_sort_asc(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: #=============== Yang dilengkapi
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j+1] = key #=============== Yang dilengkapi
     
    return data

# 2. Ubah agar menjadi descending
def insertion_sort_dsc(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] < key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j+1] = key
     
    return data

p = [90,12,142,72,856,21,100]

print("Hasil Sorting Ascending: ",insertion_sort_asc(p))
print("Hasil Sorting Ascending: ",insertion_sort_dsc(p))