# ==================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
# ==================================

# ==================================
# Latihan 3 . Tracing Insertion Sort
# ================================== 

def insertion_sort(data):

    #Print data awal
    print("Data awal: ", data)
    print("=" *50)

    for i in range(1, len(data)):
        key = data[i]

        #print iterasi dan key
        print("Iterasi ke i = ",i)
        print("Key = ", key)

        j =i-1
        while j>=0 and data[j] > key:
            
            #print data j yang akan digeser
            print("data j = ",data[j])
            
            data[j+1] = data[j]

            #print setelah pergeseran
            print("Pergeseran = ", data)

            j-=1

        data[j+1] = key

        #print setelah data disisipkan
        print("Setelah penyisipan = ", data)
        print("-"*50)

    return data

data = [5, 2, 4, 6, 1, 3] 

print("Hasil Sort = ",insertion_sort(data))


# 1. Tuliskan isi list setelah iterasi i = 1. 
# [2, 5, 4, 6, 1, 3]

# 2. Tuliskan isi list setelah iterasi i = 3. 
# [2, 4, 5, 6, 1, 3]

# 3. Berapa kali pergeseran terjadi pada iterasi i = 4? 
# Terjadi 4 kali
# Pergeseran angka 6,5,4,2