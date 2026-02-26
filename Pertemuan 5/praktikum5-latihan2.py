# ==========================================================
# Nama : Adrian Hermawan
# NIM : J0403251044
# Kelas : B1
# ==========================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ========================================================== 
 
 
def countdown(n): 
 
    if n == 0: 
        print("Selesai") 
        return 
 
    print("Masuk:", n) 
 
    countdown(n - 1) 
 
    print("Keluar:", n) 
 
 
countdown(3)

#Masuk
#countdown(3) 
    #-> Masuk:3
    #-> countdown(2)
        #-> Masuk:2
        #-> countdown(1)
            #-> Masuk:1
            #-> countdown(0)
                #-> Selesai
            #-> Keluar:1
        #-> Keluar:2
    #-> Keluar:3
    
#Kenapa print keluar angkanya terbalik?
#Karena print("Keluar:", n) berada setelah recursive call, 
# maka program akan menyelesaikan recursive call dulu sampai ketemu base case, 
# baru lanjut ke program selanjutnya