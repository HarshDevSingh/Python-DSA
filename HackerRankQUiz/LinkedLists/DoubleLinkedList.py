class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        return

    def inserting_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data)
        node.prev = itr
        itr.next = node
        return

    def delete_at(self,index):
        if self.head is None:
            return f"Dll is empty"
        l=self.get_len()-1
        if index>l or index<0:
            return f"index is out of scope"
        counter=0
        itr=self.head
        while itr:
            if counter==index-1:
                itr.next=itr.next.next
                return
            counter+=1
            itr=itr.next

    def get_len(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def print_dll(self):
        itr = self.head
        res = ""
        while itr:
            suffix = "<-->" if itr.next else ""
            pdata = str(itr.prev.data) if itr.prev else ""
            ndata = str(itr.next.data) if itr.next else ""
            res += pdata + "|" + str(itr.data) + "|" + ndata + suffix
            itr = itr.next
        return res


dll = DLinkedList()
dll.insert_at_begining(1)
dll.insert_at_begining(2)
dll.insert_at_begining(3)
dll.insert_at_begining(4)
dll.insert_at_begining(5)
dll.inserting_at_end(0)
dll.inserting_at_end(-1)
print(dll.print_dll())
dll.delete_at(1)
print(dll.print_dll())

# print(dll.get_len())
