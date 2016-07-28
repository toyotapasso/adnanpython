class Node:

    def __init__(self, id):
        self.id = id
        self.neighbours = []
        self.distance = 0


    def __str__(self):
        return str(self.id)

uno = Node(1)
due = Node(2)
tri = Node(3)
qua = Node(4)

print(uno)