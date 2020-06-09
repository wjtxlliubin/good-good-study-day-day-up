class Node():
    def __init__(self, item,left=None,right=None):
        self.root = item
        self.left = left
        self.right = right


class TreeLinkList():
    def __init__(self,dict_tree=None):
        self.head = Node(
            item=dict_tree.get('element'),
            left=self.generate(dict_tree.get('left')),
            right=self.generate(dict_tree.get('right'))
        )

    def generate(self,dict_tree):
        if isinstance(dict_tree.get('left'),dict) and isinstance(dict_tree.get('right'),dict):
            return Node(
                item=dict_tree.get('element'),
                left=self.generate(dict_tree.get('left')),
                right=self.generate(dict_tree.get('right'))
            )
        elif isinstance(dict_tree.get('left'),dict) and not isinstance(dict_tree.get('right'),dict):
            return Node(
                item=dict_tree.get('element'),
                left=self.generate(dict_tree.get('left')),
                right=Node(item=dict_tree.get('right'),left=None,right=None) if dict_tree.get('right') else None
            )
        elif isinstance(dict_tree.get('right'),dict) and not isinstance(dict_tree.get('left'),dict):
            return Node(
                item=dict_tree.get('element'),
                left=Node(item=dict_tree.get('left'),left=None,right=None) if dict_tree.get('left') else None,
                right=self.generate(dict_tree.get('right'))
            )
        else:
            return Node(
                item=dict_tree.get('element'),
                left=Node(item=dict_tree.get('left'),left=None,right=None),
                right=Node(item=dict_tree.get('right'),left=None,right=None),
            )

    def front(self):
        result = []
        root = self.head
        def handle(root):
            if not root:
                return result
            else:
                result.append(root.root)
                handle(root.left)
                handle(root.right)
                return result
        return handle(root)

    def middle(self):
        result = []
        root = self.head
        def handle(root):
            if root == None:
                return result
            else:
                handle(root.left)
                result.append(root.root)
                handle(root.right)
                return result
        return handle(root)

    def behind(self):
        result = []
        root = self.head

        def handle(root):
            if root == None:
                return result
            else:
                handle(root.left)
                handle(root.right)
                result.append(root.root)
                return result

        return handle(root)

if __name__ == '__main__':
    dict_tree = {
        "element": 0,
        "left": {
            "element": 1,
            "left": {
                "element": 3,
                "left": 6,
                "right": 7,
            }
        },
        "right": {
            "element": 2,
            "left": 4,
            "right": {
                "element": 5,
                "left": 8,
                "right": 9,
            },
        },
    }
    tree = TreeLinkList(dict_tree)
    print(tree.front())
    print(tree.middle())
    print(tree.behind())





