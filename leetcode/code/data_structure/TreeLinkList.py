class Node():
    def __init__(self, item):
        self.root = item
        self.left = None
        self.right = None

class TreeLinkList():
    def __init__(self,item):
        self._head = Node(item)

    def is_empty(self):
        return self._head.root is None





