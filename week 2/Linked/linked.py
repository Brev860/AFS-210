
class Node:
    def __init__(self, data):
        self.data = data
        self.nextdata = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printlist = self.head
        while printlist is not None:
            print (printlist.data)
            printlist = printlist.nextdata
    
    def deleteNode(self, rData):  
        r = rData
        if (r is not None):
            

        

          
       
list = LinkedList()
list.head = Node("PHP")
e2 = Node("Python")
e3 = Node("C#")
e4 = Node("C++")
e5 = Node("Java")


list.head.nextdata = e2
e2.nextdata = e3
e3.nextdata = e4
e4.nextdata = e5

list.listprint()
list.deleteNode(e3)
list.listprint()
