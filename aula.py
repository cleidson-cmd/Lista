class node: #classe do nor===========================
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


    def getData(self): #retorna a posiçao do dado
        return self.data

    
    def getNext(self):  #retorna a posiçao do proximo
        return self.next


    def setData(self, newData):
        self.data = newData #new data recebe  inidata que foi criado no __init__


    def setNext(self, newNext):
        self.next = newNext #o newnext recebe o next que foi criado no __init__ 


#temp = node(2) #arquivo temporario pega  dado 
#temp.getData() #p
#print(temp.getData())


#criando classe da lista desordenada================
class unorderedlist:
    def __init__(self):
        self.head = None #cabeça inicio da lista

    def isEmpty(self):
        return self.head == None  #retorna verdadeiro apenas quando a lista estiver vazia


    def add(self, item):   
        temp = node(item)    #adiciona o valor item no node e atribui a uma variavel temporaria temp
        temp.setNext(self.head)  #insere o cabeçalho como valor do proximo
        self.head = temp    #o cabeçalho recebe a variavel temporaria que esta com o valor inserido 


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count


    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found 


    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()
            
        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())


lista = unorderedlist()

lista.add(28)
lista.add(23)
lista.add(55)
lista.remove(28)
print(lista.size())
print(lista.search(23))
print(lista.isEmpty())


