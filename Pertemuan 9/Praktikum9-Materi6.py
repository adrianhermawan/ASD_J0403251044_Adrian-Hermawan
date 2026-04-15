#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
#====================================================
# Latihan 6: Struktur Organisasi Perusahaan
#====================================================

#Class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data= data    #menyimpan nilai node
        self.left = None #child kiri
        self.right = None # child kanan

#fungsi preorder : root=> left => right
def preoder(node):
    if node is not None:
        print(node.data, end=" ") #root
        preoder(node.left) #left
        preoder(node.right) #right


#membuat tree
#membuat root
root = Node("Direktur")

#membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

#lanjutan child kanan level 2
root.right.right = Node("Staff 3")


print("Struktur Perusahaan")
preoder(root)