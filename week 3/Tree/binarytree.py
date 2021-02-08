class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None
  




class BSTTree:
    def __init__(self):
        super().__init__()
        self.root = None

    def sortedArrayToBST(self, arr): 
        if not arr: 
          return None
      
        mid = int(len(arr) / 2)
     
        root = Node(arr[mid])
        root.left = bst.sortedArrayToBST(arr[:mid]) 
   
        root.right = bst.sortedArrayToBST(arr[mid+1:]) 
        return root 
 
    def preOrder(self, node): 
       if node:   
          return node.data, bst.preOrder(node.left), bst.preOrder(node.right)

bst = BSTTree()
arr = [1, 2, 3, 4, 5, 6, 7] 
root = bst.sortedArrayToBST(arr) 
print(bst.preOrder(root))
