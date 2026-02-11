class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node= Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def tambah_list(self, other_list):
        if not self.head:
            return other_list.head
        
        temp = self.head
        while temp.next:
            temp = temp.next #cari angka terakhir dari list 1
        
        temp.next = other_list.head
        return self.head
            
def input_list(pesan):
    data_input = input(pesan)
    
    if data_input.strip() == "":
        return []
    
    return [int(x.strip()) for x in data_input.split(",") if x.strip() != ""]

list1 = LinkedList()
list2 = LinkedList()

data1 = input_list("Masukkan elemen untuk Linked List 1: ")
data2 = input_list("Masukkan elemen untuk Linked List 2: ")

for x in data1:
    list1.insert_at_end(x)
    
for x in data2:
    list2.insert_at_end(x)

print("Linked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

list1.tambah_list(list2)

print("Linked List setelah digabungkan: ", end=" ")
list1.display()
