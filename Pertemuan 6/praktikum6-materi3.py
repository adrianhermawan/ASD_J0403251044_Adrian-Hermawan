# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Merge Sort (Ascending)
# ==================================


def merge_sort(data):

    if len(data)<=1:
        return data

    #Divide = membagi data menjadi 2 bagian
    mid = len(data) //2
    left=data[:mid] #slicing bagian kiri
    right=data[mid:] #slicing bagian kanan

    # 9 ==> left 4 right 4
    # left 4 ==> mergesort ==> left 2 right 2 
    # left 2 ==> left 1 right 1

    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

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


angka = [90,12,142,72,856,21,100]
print("Hasil Sorting: ",merge_sort(angka))