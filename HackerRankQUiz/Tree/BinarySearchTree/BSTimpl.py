'''
BST features:
1)smaller nodes are always on left side
2) No duplicate data
search Complexity : O(logn)
Insertion Complexity : O(logn)
'''


class BSTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return f"{data} already exists"
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTnode(data)
        else:
            self.right = BSTnode(data)

    def in_order_traversal(self):
        elements = []
        # left node
        if self.left:
            elements += self.left.in_order_traversal()
        # root
        elements.append(self.data)
        # right node
        if self.right:
            elements += self.right.in_order_traversal()
        return elements


def build_tree(elements):
    root = BSTnode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


nums = [17, 4, 1, 20, 9, 23, 18, 34]

tree = build_tree(nums)
print(tree.in_order_traversal())
