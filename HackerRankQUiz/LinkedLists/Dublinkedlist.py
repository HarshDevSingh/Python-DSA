class Node:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.next = nxt
        self.prev = prev


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def print_dll(self):
        itr = self.head
        while itr:
            print(itr.prev.value if itr.prev else None, \
                  "<- prev", itr.value, "next ->", \
                  itr.next.value if itr.next else None)
            itr = itr.next

    def insert_at_last(self, value):
        if self.head is None:
            self.insert_at_start(value)
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def get_dll_len(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def insert_at_loc(self, idx, value):
        if idx == 0:
            self.insert_at_start(value)
        if idx == self.get_dll_len() - 1:
            self.insert_at_last(value)
        else:
            itr = self.head
            counter = 0
            while itr.next:
                if counter == idx - 1:
                    newNode = Node(value)
                    newNode.next = itr.next
                    newNode.prev = itr.next.prev
                    itr.next = newNode
                counter += 1
                itr = itr.next

    def print_tail(self):
        return self.tail.value


d = Dll()
d.insert_at_start(1)
d.insert_at_start(2)
d.insert_at_start(3)
d.insert_at_last(0)
d.insert_at_loc(0, 5)
d.insert_at_loc(4, 6)
d.insert_at_loc(2, 7)

d.print_dll()
print(d.print_tail())
