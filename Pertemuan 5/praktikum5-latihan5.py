# ==========================================================
# Nama : Adrian Hermawan
# NIM : J0403251044
# Kelas : B1
# ==========================================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
#Cegah angka berulang ex: tidak boleh 111,222,001

def buat_pin(panjang, hasil=""): 
    #panjang = panjang pin yang diinginkan
    #hasil = variabel string sementara untuk menyimpan pin saat program berjalan

    #base case
    #kalau panjang hasil sudah sesuai dengan panjang yang diminta
    if len(hasil) == panjang: 
        #print pin yang sudah dibuat otomatis
        print("PIN:", hasil) 
        return 
    
    
    for angka in ["0", "1", "2"]:
        #pencegahan
        #kalau angkanya sudah terpakai, akan di skip dan lanjut ke angka selanjutnya 
        if angka not in hasil:
            buat_pin(panjang, hasil + angka) 
 
 
buat_pin(3) 
 
