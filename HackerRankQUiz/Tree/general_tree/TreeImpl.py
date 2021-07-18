class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        sp = " " * self.get_level() * 3
        suffix=sp+"|_" if self.parent else ""
        print(suffix, self.data)
        for child in self.children:
            child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("laptop")
    mac = TreeNode("mac")
    win = TreeNode("win")
    laptop.add_child(mac)
    laptop.add_child(win)
    Tv = TreeNode("TV")
    LG = TreeNode("LG")
    SAMSUNG = TreeNode("SAMSUNG")
    Tv.add_child(LG)
    Tv.add_child(SAMSUNG)
    root.add_child(laptop)
    root.add_child(Tv)
    root.print_tree()
    return root


tree = build_product_tree()
print()
