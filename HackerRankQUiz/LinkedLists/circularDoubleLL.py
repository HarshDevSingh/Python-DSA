class Node:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.next = nxt
        self.prev = prev


class CDll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.head.prev = self.tail
            self.tail.next = self.head

    def insert_at_last(self, value):
        if self.head is None:
            self.insert_at_start(value)
            return
        itr = self.head
        while itr.next:
            if itr == self.tail:
                newNode = Node(value)
                newNode.next = self.head
                newNode.prev = itr
                itr.next = newNode
                self.tail = newNode
                self.head.prev = newNode
                break
            itr = itr.next
        return

    def find_element(self, value):
        if self.head is None:
            return False
        else:
            itr = self.head
            while itr:
                if itr.value == value:
                    return True
                if itr == self.tail:
                    break
                itr = itr.next
            return False

    def get_element_by_index(self, idx):
        if self.head is None:
            return
        elif idx >= self.get_dll_len():
            return
        else:
            itr = self.head
            counter = 0
            while itr:
                if counter == idx:
                    return itr.value
                if itr == self.tail:
                    break
                counter += 1
                itr = itr.next
        return

    def delete_at(self, idx):
        if not self.head:
            return
        else:
            if idx == 0:
                self.head = self.head.next
                self.head.next = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                return
            else:
                counter = 0
                itr = self.head
                while itr:
                    if counter == idx - 1 and itr.next != self.tail:
                        print(counter == idx - 1, "-->", itr.value)
                        itr.next = itr.next.next
                        itr.next.prev=itr
                        return
                    if itr.next == self.tail:
                        self.tail = itr
                        self.tail.next = self.head
                        self.head.prev = self.tail
                        break
                    if itr == self.tail:
                        break
                    counter += 1
                    itr = itr.next

    def get_dll_len(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            if itr == self.tail:
                break
            itr = itr.next
        return counter

    def print_dll(self):
        if not self.head:
            return []
        itr = self.head
        while itr:
            print(itr.prev.value if itr.prev else None, \
                  "<- prev", itr.value, "next ->", \
                  itr.next.value if itr.next else None)
            if itr.next == self.tail.next:
                break
            itr = itr.next

    def delete_all(self):
        self.head = None
        self.tail = None


cdll = CDll()
cdll.insert_at_start(2)
cdll.insert_at_start(1)
cdll.insert_at_start(0)
cdll.insert_at_last(3)
cdll.print_dll()
print(cdll.find_element(3))
print(cdll.get_element_by_index(3))
cdll.delete_all()
print(cdll.print_dll())
cdll.insert_at_start(2)
cdll.insert_at_start(1)
cdll.insert_at_start(0)
cdll.insert_at_last(3)
cdll.insert_at_last(4)
cdll.insert_at_last(5)
cdll.delete_at(4)
cdll.print_dll()
