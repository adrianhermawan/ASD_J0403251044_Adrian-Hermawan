#====================================================
# Nama: Adrian Hermawan
# NIM: J0403251044
# Kelas: B1
#====================================================
# Latihan 2: Membuat Node Tree
#====================================================

#Class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data= data    #menyimpan nilai node
        self.left = None #child kiri
        self.right = None # child kanan
    
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#lanjutan child kanan level 2
root.right.left = Node("F")
root.right.right = Node("G")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left.data)
print("Data child kanan root", root.right.data)
print("Data child kiri dari B:", root.left.left.data)
print("Data child kanan dari B:", root.left.right.data)

#tugas
print("Data child kiri dari C:", root.right.left.data)
print("Data child kanan dari C:", root.right.right.data)



#lanjutkan kode programnya untuk keseluruhan bagian kanan, F dan G

#penjelasan------------------------------
#membuat tree lengkap
#membuat data child hingga level 2, root.left = child kiri, root.right = child kanan
# root.left.left = child kiri dan kiri lagi, dst.