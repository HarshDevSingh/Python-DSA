class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class Cll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_cll_start(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head
        else:
            self.head = Node(value, self.head)
            self.tail.next = self.head

    def insert_into_cll_at_last(self, value):
        if not self.head:
            self.insert_in_cll_start(value)
        else:
            itr = self.head
            while itr:
                if itr == self.tail:
                    break
                itr = itr.next
            itr.next = Node(value, self.tail.next)
            self.tail = self.tail.next

    def insert_by_index(self, idx, value):
        if idx == 0:
            self.insert_in_cll_start(value)
        elif idx == self.len_of_cll() - 1:
            self.insert_into_cll_at_last(value)
        elif idx >= self.len_of_cll() or idx < 0:
            raise IndexError("either index is greater than length of cll or invalid value provided")
        else:
            counter = 0
            itr = self.head
            while itr.next:
                if itr == self.tail:
                    break
                if counter == idx - 1:
                    itr.next = Node(value, itr.next)
                    return
                counter += 1
                itr = itr.next

    def delete_element(self, idx):
        if idx == 0:
            self.head = self.head.next
            self.tail.next = self.head
            return
        if idx >= self.len_of_cll() or idx < 0:
            raise IndexError("either index is greater than length of cll or invalid value provided")
        else:
            itr = self.head
            counter = 0
            if idx == self.len_of_cll() - 1:
                while itr:
                    if itr.next ==self.tail:
                        self.tail=itr
                        self.tail.next=self.head
                        return
                    itr = itr.next
            while itr:
                if counter == idx - 1:
                    itr.next = itr.next.next
                    return
                counter += 1
                itr = itr.next

    def delete_all(self):
        self.head=None
        self.tail=None
        return

    def len_of_cll(self):
        if not self.head:
            return 0
        else:
            counter = 0
            itr = self.head
            while itr:
                counter += 1
                if itr == self.tail:
                    break
                itr = itr.next
        return counter

    def print_cll(self):
        if not self.head:
            return []
        else:
            ele = []
            itr = self.head
            while itr:
                ele.append(itr.value)
                if itr == self.tail:
                    print(f"end of CLL reached and last node {self.tail.value} points back to", itr.next.value)
                    break
                itr = itr.next
        return ele


cll = Cll()
cll.insert_in_cll_start(1)
cll.insert_in_cll_start(2)
cll.insert_in_cll_start(3)
cll.insert_in_cll_start(4)
cll.insert_into_cll_at_last(0)
cll.insert_in_cll_start(1)
cll.insert_into_cll_at_last(-1)
cll.insert_into_cll_at_last(-2)
cll.insert_by_index(0, 9)
cll.insert_by_index(1, 10)
cll.insert_by_index(5, 11)
print(cll.print_cll())
print(cll.len_of_cll())
cll.delete_element(cll.len_of_cll()-1)
print(cll.print_cll())
print(cll.len_of_cll())
cll.delete_element(2)
print(cll.print_cll())
print(cll.len_of_cll())
cll.delete_element(0)
print(cll.print_cll())
print(cll.len_of_cll())
cll.delete_all()
print(cll.print_cll())
print(cll.len_of_cll())