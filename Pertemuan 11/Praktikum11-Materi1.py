#===============================================
#Nama : Adrian Hermawan
#NIM : J0403251044
#Kelas : B / P1

#===============================================
#Implemantasi Dasar Graph
#===============================================

graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C']
}

for node in graph:
    print(node, "->", graph[node])