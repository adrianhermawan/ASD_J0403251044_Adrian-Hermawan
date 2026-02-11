class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node= Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        if not self.head:
            print("List Empty")
            return
        
        print("\nCircular Linked List Traversal:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        
        while temp!= self.head:
            print(temp.data, end=" -> ")
            temp=temp.next
        
        print("...(back to head)")
    
    def search(self, key):
        temp = self.head
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List")
        return

data_input = input("Masukkan elemen ke dalam Circular Linked List: ")
if data_input.strip() == "":
    data_list = []
else:
    data_list = [int(x.strip()) for x in data_input.split(",") if x.strip() != ""] #untuk menghapus data kosong kalau input 1,2,3, (koma di belakang, list = [1, 2, 3, ])
#print(data_list)

cll = CircularLinkedList()
for data in data_list:
    cll.insert_at_end(data)

key = int(input("Masukkan elemen yang ingin dicari: "))
#cll.display()

cll.search(key)

