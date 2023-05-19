#'Introduction to programming':Task 5
#Seriakov Vlad, FB-21, V-4

class Node:
    def __init__(self, e):
        self.e = e
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, e):
        if not self.root:
            self.root = Node(e)
        else:
            self._add(e, self.root)

    def _add(self, e, node):
        if e < node.e:
            if node.leftChild:
                self._add(e, node.leftChild)
            else:
                node.leftChild = Node(e)
        else:
            if node.rightChild:
                self._add(e, node.rightChild)
            else:
                node.rightChild = Node(e)
    
    def search(self, e):
        return self._search(e, self.root)
    
    def _search(self, e, node):
        if not node:
            return False
        elif node.e == e:
            return True
        elif e < node.e:
            return self._search(e, node.leftChild)
        else:
            return self._search(e, node.rightChild)
        
    def delete(self, e):
        if not self.root:
            return False
        else:
            self.root = self._delete(e, self.root)
    
    def _delete(self, e, node):
        if not node:
            return node
        if e < node.e:
            node.leftChild = self._delete(e, node.leftChild)
        elif e > node.e:
            node.rightChild = self._delete(e, node.rightChild)
        else:
            if not node.leftChild:
                return node.rightChild
            elif not node.rightChild:
                return node.leftChild
            else:
                temp = self._get_min(node.rightChild)
                node.e = temp.e
                node.rightChild = self._delete(temp.e, node.rightChild)
        return node
    
    def _get_min(self, node):
        temp = node
        while temp.leftChild:
            temp = temp.leftChild
        return temp
    
L = BinarySearchTree()
L.add(1)
L.add(4)
L.add(10)
L.add(14)
L.add(20)
L.add(24)
L.add(130)
L.add(250)
print(L.search(1))
print(L.search(130))
print(L.search(24))
print(L.search(251))
print(L.search(14))
L.delete(14)
print(L.search(14))