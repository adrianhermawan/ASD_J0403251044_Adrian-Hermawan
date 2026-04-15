#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
#====================================================
# Latihan 5: Transversal Postorder
#====================================================

#Class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data= data    #menyimpan nilai node
        self.left = None #child kiri
        self.right = None # child kanan

#membuat fungsi postorder: left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left) #kiri
        postorder(node.right) #kanan
        print(node.data, end=" ") #root

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

#menjalankan transversal postorder
print("Hasil Traversal Postorder")
postorder(root)

#penjelasan---------------------------------------------
#inorder = kiri -> kanan -> root
# jadi mulai dari ujung kiri, ke kanan, lalu ke root
# root selalu diakhir setelah kiri dan kanan
# root.left.left -> root.left -> root.left.right -> root -> root.right -> root.right.right