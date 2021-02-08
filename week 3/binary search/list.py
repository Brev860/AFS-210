class BSTNode:
    def __init__(self, val = None):
        super().__init__()
        self.val = val
        self.left = None
        self.right = None


class BSTTree:
    def __init__(self):
        super().__init__()
        self.root = None


    def add(self, val):
        if self.root is None:
            self.root = BSTNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, cur_node):
        if val < cur_node.val:
            if cur_node.left is None:
                cur_node.left = BSTNode(val)
            else:
                self._add(val, cur_node.left)
        elif val > cur_node.val:
            if cur_node.right is None:
                cur_node.right = BSTNode(val)
            else:
                self._add(val, cur_node.right)
        else:
            print("Data already exists in tree")
    def locate(self, val):
        if self.root:
            is_found = self._find(val, self.root)
            if is_found:
                return val
            return False
        else:
            return None
    def _find(self, val, cur_node):
        if val > cur_node.val and  cur_node.right:
            return self._find(val, cur_node.right)
        elif val < cur_node.val and cur_node.left:
            return self._find(val, cur_node.left)

        if val == cur_node.val:
            return True
    def print_tree(self, trav_type):
        if trav_type == "preorder":
            return self.printout(BST.root, "")
        else:
            print("Doesnt exist")
            return False
    def printout(self, start, trav):
        if start:
            trav += (str(start.val) + "-")
            trav = self.printout(start.left, trav)  
            trav = self.printout(start.right, trav)
        return trav
a = [4,2,3,1,6,7,5]
BST = BSTTree()

for i in a:
    BST.add(i) 

# BST.add(3)
# BST.add(1)
# BST.add(4)
# BST.add(6)
# BST.add(17)
# BST.add(9)
# BST.add(2)

print(BST.print_tree("preorder"))