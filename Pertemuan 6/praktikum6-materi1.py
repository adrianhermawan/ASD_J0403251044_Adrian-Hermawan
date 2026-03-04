# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Insertion Sort (Ascending)
# ==================================

def insertion_sort(data):
    #Loop mulai dari data ke 2
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index elemen terakhir di bagian kiri (sorted)
        
        while j>=0 and data[j]>key:
            data[j+1] = data[j]
            j -=1
        
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

p = [1,6,4,7,32,17]

print("Hasil Sorting: ",insertion_sort(p))