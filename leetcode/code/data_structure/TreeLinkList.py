class Node():
    def __init__(self, item,left=None,right=None):
        self.root = item
        self.left = left
        self.right = right

class TreeLinkList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head.root is None

    def add(self,item,left=None,right=None):
        if self.is_empty():
            self._head = Node(item,left=left,right=right)
        else:
            raise Exception('root is not None of head')

    def append(self,):
        pass




