# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Latihan 5 . Melengkapi Fungsi Merge 
# ================================== 

def merge_sort(data): 
    if len(data) <= 1: 
        return data 
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 

    return merge(left_sorted, right_sorted) 


# 1. Lengkapi kondisi agar menjadi ascending
def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: #============ Yang dilengkapi 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result 

data = [5, 2, 4, 6, 1, 3] 

print("Hasil Sort = ",merge_sort(data))

# 2.Jelaskan fungsi result.extend()
# result.extend() digunakan untuk menambahkan sisa elemen yang belum masuk ke result
# saat salah satu list (right atau left) sudah habis