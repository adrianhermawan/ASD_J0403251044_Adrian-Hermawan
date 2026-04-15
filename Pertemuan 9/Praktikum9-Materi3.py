#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
#====================================================
# Latihan 3: Fungsi Transversal Preorder
#====================================================

#Class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data= data    #menyimpan nilai node
        self.left = None #child kiri
        self.right = None # child kanan\

#fungsi preorder : root=> left => right
def preoder(node):
    if node is not None:
        print(node.data, end=" ") #root
        preoder(node.left) #left
        preoder(node.right) #right

#membuat tree
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#lanjutan child kanan level 2
root.right.right = Node("F")

#menjalankan transversal preorder
print("Hasil Traversal Preoder")
preoder(root)

#penjelasan--------------------------------------------------
#transversal preorder = Menampilkan tree mulai dari root -> left -> right
# jadi print root dulu
# root -> root.left -> root.left.left -> root.left.right ->root.right