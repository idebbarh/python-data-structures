class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None :
            self.head = Node(data,None)
        else :
            itr = self.head
            while itr.next :
                itr = itr.next
            itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_len(self):
        counter = 0
        itr = self.head 
        while itr :
            counter+=1
            itr = itr.next
        return counter

    def insert_at(self,index,data):
        if index < 0 or index > self.get_len() :
            raise Exception("Index Out Of Range")
        if index == 0 :
            self.insert_at_begining(data)
            return
        itr = self.head
        count = 0
        while count < index-1 :
            itr = itr.next
            count+=1
        node = Node(data,itr.next)
        itr.next = node

    def insert_values(self,data_list):
        for data in data_list :
            self.insert_at_end(data)
    
    def insert_after_value(self,after_what,data) :
        found = False 
        itr = self.head
        while itr :
            if itr.data == after_what :
                found = True
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
        if not found :
            raise Exception("The Value Not In The Linkedlist")

    def insert_before_value(self,before_what,data):
        found = False
        itr = self.head
        if self.head.data == before_what :
            self.insert_at_begining(data)
        else :
            while itr.next :
                if itr.next.data == before_what :
                    found = True
                    itr.next = Node(data,itr.next)
                    break
                itr = itr.next
            if not found :
                raise Exception("The Value Not In The Linkedlist")

    def delete_last(self):
        if self.head is None :
            print("Linked List is Empty")
            return 
        if self.head.next is None :
            self.head = None
        else :
            itr = self.head
            while True :
                if itr.next.next is None :
                    break
                itr = itr.next
            itr.next = None

    def delete_first(self):
        if self.head is None :
            print("Linked List is Empty")
            return
        self.head = self.head.next

    def delete_by_index(self,index):
        if index < 0 or index > self.get_len():
            raise Exception("Index Out Of Range")
        if index == 0 :
            self.delete_first()
            return
        if index == self.get_len():
            self.delete_last()
            return
        itr = self.head
        count = 0
        while count < index-1 :
            count+=1
            itr = itr.next
        itr.next = itr.next.next

    def delele_by_value(self,value):
        found = False
        itr = self.head
        while itr.next :
            if itr.next.data == value :
                itr.next = itr.next.next
                found = True
                break
            itr = itr.next
        if not found :
            raise Exception("The Value Not In The Linkedlist")
    
    def get_by_index(self,index):
        if index < 0 or index+1 > self.get_len():
            raise Exception("Index Out Of Range")
        if self.head is None :
            print("Linked List Is Empty")
        itr = self.head
        count = 0
        while itr :
            if count == index :
                print(itr.data)
                break
            count+=1
            itr = itr.next

    def replace_element_by_element(self,old_data,new_data) :
        if self.head.data == old_data :
            self.head = Node(new_data,self.head.next) 
        else :
            found = False
            itr = self.head
            while itr.next :
                if itr.next.data == old_data :
                    itr.next = Node(new_data,itr.next.next)
                    found = True
                    break
                itr = itr.next
            if not found :
                raise Exception("The Value Not In The Linkedlist")

    def reverse_linkedlist(self):
        curr = self.head
        prev = None
        while curr :
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        d= ""
        while prev:
            d += prev.data+"<==" if prev.next else prev.data
            prev = prev.next
        print(d)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end("1")
    ll.insert_at_end("2")
    ll.insert_at_end("3")
    ll.reverse_linkedlist()




