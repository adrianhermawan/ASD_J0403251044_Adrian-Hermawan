#=======================================================================================
# Nama   : Adrian Hermawan
# NIM    : J0403251044
# Kelas  : TPL B/P1
#=======================================================================================

#=======================================================================================
# Latihan 1 : BST
#=======================================================================================

#node untuk bst
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    #jika root kosong, buat node baru
    if root is None:
        return Node(data)
    
    #kalau data lebih kecil dari root, turun ke kiri
    if data < root.data:
        root.left = insert(root.left,data)

    #kalau data lebih besar dari root, turun ke kanan
    elif data > root.data:
        root.right = insert(root.right,data)

    return root

#Mengisi data pada BST 
root = None
data_list = [50,30,70,20,40,60,80]

for data in data_list:
    root = insert(root,data)

print("BST berhasil dibuat")


#========================================
#Latihan 2 : tranversal inorder
#========================================

def inorder(root):
    #berjalan saat root tidak kosong
    if root is not None:
        #print dari kiri, root, kanan
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print ("Hasil Inorder: ")
inorder(root)

#========================================
#Latihan 3 : Search di BST
#========================================

def search(root,key):
    #menjaga agar tidak error saaat root kosong
    if root is None:
        return False
    
    #kalau ketemu, return true
    if root.data == key:
        return True
    
    #kalau key lebih kecil dari root, cari ke sebelah kiri
    if key < root.data:
        return search (root.left,key)
    
    #kalau key lebih besar dari root, cari ke sebelah kanan
    else:
        return search (root.right,key)
    
# Uji pencarian
key = 40
if search (root,key):
    print("Data ditemukan")
else:
    print("Data ditemukan")