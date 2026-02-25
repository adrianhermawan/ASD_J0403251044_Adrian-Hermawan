#====================================================
#Nama: Adrian Hermawan
#NIM: J0403251044
#Kelas: B1
#====================================================

#====================================================
#Materi Rekursif : Faktorial
# 3! = 3x2x1
#====================================================

def faktorial(n):    
    #base case
    if n == 0:
        return 1
    
    #recursive case
    return n*faktorial(n-1)

print("Hasil Faktorial: ", faktorial(3))