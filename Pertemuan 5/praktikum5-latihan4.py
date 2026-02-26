# ==========================================================
# Nama : Adrian Hermawan
# NIM : J0403251044
# Kelas : B1
# ==========================================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
    # n = panjang huruf yang ingin dihasilkan
    # hasil = string sementara
    
    #base case
    # n = 2
    # kalau panjang hasil = 2, recursive call berhenti
    if len(hasil) == n: 
        # Artinya satu kombinasi sudah lengkap
        # Cetak hasilnya (misal: "AA", "AB", dll)
        print(hasil) 
        return 
    
    #recursive call
    
    #Tambahkan huruf "A" ke hasil, lalu lanjutkan rekursi
    kombinasi(n, hasil + "A")
    
    #Tambahkan huruf "B" ke hasil, lalu lanjutkan rekursi
    kombinasi(n, hasil + "B") 
 
 
kombinasi(2)
# kenapa n=2 ada 4 kombinasi?
# 2^n
# n = 2 ==> 2^2 = 4
# n = 4 ==> 2^4 = 16 

# kombinasi(2, "")
#   kombinasi(2, "A")
#       kombinasi(2, "AA") → len("AA") == 2 → print("AA")
#       kombinasi(2, "AB") → len("AB") == 2 → print("AB")
#   kombinasi(2, "B")
#       kombinasi(2, "BA") → len("BA") == 2 → print("BA")
#       kombinasi(2, "BB") → len("BB") == 2 → print("BB")