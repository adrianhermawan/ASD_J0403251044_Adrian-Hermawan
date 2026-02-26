# ==========================================================
# Nama : Adrian Hermawan
# NIM : J0403251044
# Kelas : B1
# ==========================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 

def pangkat(a, n): 
#a = bilangan
#n = pangkatnya

# Base case 
    if n == 0: # karna a pangkat 0 = 1
        return 1 

# Recursive case 
    return a * pangkat(a, n - 1) 

print(pangkat(2, 4))  # Output: 16

#recursive call
#pangkat(2,4) = 2 * pangkat(2,3)
#pangkat(2,3) = 2 * pangkat(2,2)
#pangkat(2,2) = 2 * pangkat(2,1)
#pangkat(2,1) = 2 * pangkat(2,0)

#pangkat(2,0) = 1 #nyentuh base case

#hasil
#pangkat(2,4) = 2 * 2 * 2 * 2 * 1 = 16 