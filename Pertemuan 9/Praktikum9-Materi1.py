#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
#====================================================
# Latihan 1: Membuat Node
#====================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data= data    #menyimpan nilai node
        self.left = None #child kiri
        self.right = None # child kanan
    
#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#Penjelasan-------------------------------------------
#membuat class node karena data tree dasar datanya adalah node
#root adalah data paling atas dalam sebuah tree
#root.left dan root.right sudah ada namun berisi None