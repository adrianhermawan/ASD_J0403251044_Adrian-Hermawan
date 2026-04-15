#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
#====================================================
# Latihan 4: Transversal Inorder
#====================================================

#Class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data= data    #menyimpan nilai node
        self.left = None #child kiri
        self.right = None # child kanan

#membuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left) #left
        print(node.data, end=" ") #root
        inorder(node.right) #right

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

#menjalankan transversal inorder
print("Hasil Traversal Inorder")
inorder(root)

#penjelasan------------------------------
#inorder = kiri -> root -> kanan
# jadi mulai dari ujung kiri, ke root, lalu ke kanan
# root selalu ditengah antara kiri dan kanan
# root.left.left -> root.left -> root.left.right -> root -> root.right -> root.right.right