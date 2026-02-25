#====================================================
#Nama: Adrian Hermawan
#NIM: J0403251044
#Kelas: B1
#====================================================

#====================================================
#Materi Rekursif : Call Stack
#Tracing bilangan (masuk-keluar)
#input 3
#Masuk 1-2-3
#Keluar 3-2-1
#====================================================

def hitung(n):

    #base case
    if n == 0:
        print("Selesai")
        return


    print("Masuk:",n)
    hitung(n-1) #recursive case
    print("Keluar:", n)

print("===========Program Tracing==============")
hitung(3)