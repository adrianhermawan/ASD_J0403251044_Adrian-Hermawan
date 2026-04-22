#=======================================================================================
# Nama   : Adrian Hermawan
# NIM    : J0403251044
# Kelas  : TPL B/P1
#=======================================================================================

#=======================================================================================
# Latihan 4 : Membuat BST yang tidak seimbang
#=======================================================================================

# Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk BST 
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    return root 
 
 
# Fungsi preorder untuk melihat bentuk tree 
def preorder(root): 
    if root is not None: 

        #root, kiri, kanan
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        #print indentasi sesuai level
        print("   " * level + f"{posisi}: {root.data}") 

        #lanjut ke child left
        tampil_struktur(root.left, level + 1, "L")
        #lanjut child right
        tampil_struktur(root.right, level + 1, "R") 

# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None 
# Data dimasukkan berurutan naik 
data_list = [10, 20, 30] 

for data in data_list: 
    root = insert(root, data) 

print("Preorder BST:") 
preorder(root) 
print("\n\nStruktur BST:") 
tampil_struktur(root)

#==========penjelasan====================
#1. tree condong ke kanan, karena data yang dimasukkan berurutan naik, maka yang menjadi root adalah 10
# dan data selanjutnya lebih besar dari 10, maka akan condong ke kanan

#2. semakin panjang tree, pencarian makin lambat
# umumnya pencarian bst itu cepat (log n), tapi kalau bentuknya memanjang seperti bentuk ini, 
# pencarian harus dicek satu persatu

#3. BST tidak selalu seimbang, tergantung urutan input
# kalau inputnya urut naik/turun, strukturnya jadi tidak seimbang dan condong ke satu sisi
# supaya seimbang ada AVL