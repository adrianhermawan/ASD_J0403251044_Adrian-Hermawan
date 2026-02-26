# ==========================================================
# Nama : Adrian Hermawan
# NIM : J0403251044
# Kelas : B1
# ==========================================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): 
    #data = list yang mau dicari nilai maks nya
    #index = posisi elemen yang mau dicek, mulai dari 0
 
    # Base case 
    # kalau sudah sampai index terakhir maka program akan mengembalikan data tersebut
    if index == len(data) - 1: #-1 karna index mulainya dari 0 
        return data[index] 
 
    # Recursive case 
    #panggil fungsi ini untuk index selanjutnya, sampai nyentuh base case(index terakhir)
    # taruh data di variabel maks sisa untuk dibandingkan
    maks_sisa = cari_maks(data, index + 1) 
 
    #proses perbandingan, mulai dari index terakhir dibandingkan dengan variabel maks sisa dari case sebelumnya
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
    
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))

'''
ALUR
cari_maks(data,0)
-> bandingkan 3 dengan 
    cari_maks(data,1)
    -> bandingkan 7 dengan
        cari_maks(data,2)
        -> bandingkan 2 dengan 
            cari_maks(data,3)
            -> bandingkan 9 dengan
                cari_maks(data,4)
                -> return 5   (base case)
            -> bandingkan 9 dengan 5 ==> 9
        -> bandingkan 2 dengan 9 ==> 9
    -> bandingkan 7 dengan 9 ==> 9
-> bandingkan 3 dengan 9 ==> 9

maks data = 9
'''