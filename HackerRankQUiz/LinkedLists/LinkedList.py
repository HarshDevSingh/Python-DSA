class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def print_ll(self):
        itr = self.head
        llstr = ""
        while itr:
            suffix = "-->" if itr.next else ""
            llstr += str(itr.data) + suffix
            itr = itr.next
        return llstr

    def get_length(self):
        l = 0
        if not self.head:
            return l
        itr = self.head
        while itr:
            l += 1
            itr = itr.next
        return l

    def insert_at_end(self,data):
        itr =self.head
        if not self.head:
            self.insert_at_begining(data)
            return
        while itr.next:
            itr=itr.next
        itr.next=Node(data)
        return

    def insert_at_loc(self,index,data):
        if index <0 or index not in range(self.get_length()):
            return "invalid index"
        itr=self.head
        if index == 0:
            self.insert_at_begining(data)
            return "inserted at begining"
        if index == self.get_length()-1:
            self.insert_at_end(data)
            return "inserted at end"
        count=0
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next
        return f"{data},inserted successfully at index:{index}"

    def remove_at(self,index):
        if index <0 or index not in range(self.get_length()):
            return "invalid index"
        if index == 0:
            self.head=self.head.next
            return "node deleted successfully"
        itr=self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
        return "node deleted successfully"

    def bulk_insert(self, data_list=[], at_end=True):
        if len(data_list)<1:
            return "Please provide list of data"
        for data in data_list:
            print(data)
            if at_end:
                self.insert_at_end(data)
            else:
                self.insert_at_begining(data)
        return "data inserted, successfully!"




ll = LinkedList()
ll.insert_at_begining(4)
ll.insert_at_begining(5)
ll.insert_at_begining(6)
ll.bulk_insert(data_list=[3,2,1])
print(ll.print_ll())
ll.bulk_insert(data_list=[8,9,10],at_end=False)
print(ll.print_ll())
ll.bulk_insert(data_list=[])
print(ll.print_ll())
