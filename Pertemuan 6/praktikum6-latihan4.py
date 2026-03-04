# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Latihan 4 . Memahami Kode Program (Merge Sort) 
# ================================== 

def merge(left,right):

    result = []

    i =0
    j=0

    #Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #Menambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(data): 
    if len(data) <= 1: 
        return data 
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
     
    return merge(left_sorted, right_sorted) 

data = [5, 2, 4, 6, 1, 3] 

print("Hasil Sort = ",merge_sort(data))

# 1. Apa yang dimaksud dengan base case? 
# Base Case adalah suatu case/kondisi yang memungkinkan fungsi rekursif untuk berhenti memanggil dirinya sendiri

# 2. Mengapa fungsi memanggil dirinya sendiri? 
# Karena merge sort memakai rekursi untuk memecah data menjadi bagian kecil kecil

# 3. Apa tujuan fungsi merge()? 
# Tujuan fungsi merge adalah menggabungkan dua bagian data yang sudah pecah tadi dengan terurut