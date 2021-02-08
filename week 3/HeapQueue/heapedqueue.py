class HeapQueueMax:
    def __init__(self, data = []):
        super().__init__()
        self.heap = [0]
        self.count = 0
        for n in data:
            self.heap.append(n)
            

    def maxVal(self):
        maxItem = self.heap[0]
        maxList = []
        for x in range(1, len(self.heap)):
            if maxItem < self.heap[x]:
                maxItem = self.heap[x]
                maxList.append(maxItem)
                return maxList
            else:
                return 
                
    def view(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False


    def printList(self):
        printVal = self.heap[1:len(self.heap)]
        print(printVal)

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
        

    # def moveup(self):





a = [25, 35, 22, 85, 14, 65, 75, 22, 58]

m = HeapQueueMax(a)
print(m.maxVal())
m.printList() 


