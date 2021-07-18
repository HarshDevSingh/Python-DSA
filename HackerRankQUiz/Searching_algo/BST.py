class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
            else:
                return f"data already exists in the tree"
        else:
            self.data = data

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

b=BST(10)
b.insert(11)
b.insert(14)
b.insert(23)
b.insert(9)
b.insert(5)
b.insert(3)
b.display()