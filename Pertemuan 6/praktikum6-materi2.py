# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Insertion Sort dengan tracing
# ==================================

def insertion_sort(data):
    #melihat data awal
    print("Data awal: ", data)
    print("="*50)
    
    #Loop mulai dari data ke 2
    for i in range(1, len(data)):        

        key = data[i] #simpan nilai yang disisipkan
        
        j = i-1 #index elemen terakhir di bagian kiri (sorted)
        
        print("Iterasi ke-",i)
        print("Nilai Key = ",key)
        print("Bagian Kiri (sorted): ", data[:i])
        print("Bagian Kanan (unsorted) = ", data[i:])

        #geser
        while j>=0 and data[j]>key:
            
            
            data[j+1] = data[j]

            print("J:",data[j])
            print("Step sisipkan: ",data)
        
            j -=1
        
        #sisipkan key ke posisi yang benar
        
        data[j+1] = key

        print("Setelah disisipkan: ", data)
        print("-"*50)

    return data

p = [90,12,142,72,856,21,100]

print("Hasil Sorting: ",insertion_sort(p))