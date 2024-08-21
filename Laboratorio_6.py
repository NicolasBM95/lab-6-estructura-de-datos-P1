#Clase Nodo simple
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, e):
        self.data = e
    def getNext(self):
        return self.next
    def setNext(self, n):
        self.next = n
#Clase lista simple
class List:
    def __init__(self, head, tail, size):
        self.head = None
        self.tail = None
        self.size = 0
    def size(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def setSize(self, s):
        self.size = s
    def First(self):
        return self.head
    def Last(self):
        return self.tail
    def addFirst(self, e):
        n = Node(e)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self.size += 1
    def addLast(self, e):
        n = Node(e)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self.size += 1
    def removeFirst(self):
        if not self.isEmpty():
            temp = self.head
            self.head = temp.getNext()
            temp.setNext(None)
            self.size -= 1
            return temp.getData()
        else:
            return None
    def removeLast(self):
        if self.size==1:
            return self.removeFirst()
        else:
            temp = self.tail
            anterior = self.head
            while anterior.getNext() !=self.tail:
                anterior = anterior.getNext()
            anterior.setNext(None)
            self.tail = anterior
            self.size -= 1
            return temp.getData()
#clase stack
class Stack:
    def __init__(self):
        self.data = List(None, None, 0)

    def size(self):
        return self.data.size()
    def isEmpty(self):
        return self.data.isEmpty()
    def push(self,e):
        self.data.addFirst(e)
    def pop(self):
        return self.data.removeFirst()
    def top(self):
        if not self.isEmpty():
            return self.data.First().getData()
        else:
            return None

# creamos la pila1
pila1 = Stack()

# añadimos (2,4,6,8,10) la pila1
for i in range(2,11,+2):
    pila1.push(i)

print("pila1:")

# imprime la pila1 usando pop
while not pila1.isEmpty():
    print(pila1.pop())

class Queue:
    def __init__(self):
        self.data = List(None, None, 0)
    def size(self):
        return self.data.size()
    def isEmpty(self):
        return self.data.isEmpty()
    def enqueue(self,e):
        self.data.addLast(e)
    def dequeue(self):
        return self.data.removeFirst()
    def first(self):
        return self.data.First().getData()

#creamos la cola1
cola1 = Queue()

#añadismos (2,4,6,8,10) a la cola1
for i in range(2,11,+2):
    cola1.enqueue(i)

print("cola1:")

#imprime la cola1 usando dequeue
while not cola1.isEmpty():
    print(cola1.dequeue())