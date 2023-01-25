class Node:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data = data
        self.next = next

class Linkedlist :
    def __init__(self):
        self.head = None

    def add_at_beg(self,data):
        node = Node(None,data,self.head)
        if self.head:
            self.head.prev = node
        self.head = node

    def add_to_end(self,data):
        if self.head is None :
            self.head = Node(None,data,None)
        else :
            itr = self.head
            while itr.next :
                itr = itr.next
            itr.next = Node(itr,data,None)

    def insert_at(self,data,index):
        if index < 0 or index > self.len():
            raise Exception("Index Out Of Range")
        elif index == 0 :
            self.add_at_beg(data)
        elif index == self.len() :
            self.add_to_end(data)
        else :
            count = 0
            itr = self.head
            while count < index-1:
                count+=1
                itr = itr.next
            node = Node(itr,data,itr.next)
            itr.next.prev = node
            itr.next = node
    
    def insert_after_val(self, afterWhat, data) :
        found = False
        itr = self.head
        while itr.next :
            if itr.data == afterWhat :
                found = True
                break
            itr = itr.next
        if itr.data == afterWhat :
            found = True
        if not found :
            raise Exception("The Value Not In The Linkedlist")
        node = Node(itr,data,itr.next)
        if itr.next :
            itr.next.prev = node
        itr.next = node

    def insert_before_val(self, beforeWhat, data):
        found = False
        itr = self.head
        if itr.data == beforeWhat :
            self.add_at_beg(data)
        else :
            while itr.next :
                if itr.next.data == beforeWhat :
                    found = True
                    break
                itr = itr.next
            if itr.data == beforeWhat :
                found = True
            if not found :
                raise Exception("The Value Not In The Linkedlist")
            node = Node(itr,data,itr.next)
            itr.next.prev = node
            itr.next = node

    def delete_beg(self):
        if self.head is None :
            print("the LinkedList Is Empty")
            return 
        self.head = self.head.next
        self.head.prev = None
    def len(self):
        count = 0 
        itr = self.head 
        while itr :
            count+=1
            itr = itr.next
        return count

    def delete_last(self):
        if self.head is None :
            print("the LinkedList Is Empty")
            return 
        itr = self.head 
        while itr.next.next :
            itr = itr.next
        itr.next = None

    def delete_by_value(self,value):
        found = False
        itr = self.head
        count = 0
        while itr.next :
            if itr.next.data == value :
                found = True
                break
            itr = itr.next
            count+=1
        if not found :
            raise Exception("The Value Not In The Linkedlist")
        if count == 0 :
            self.delete_beg()
        else :
            itr.next = itr.next.next
            if itr.next :
                itr.next.prev = itr

    def print(self):
        if self.head is None :
            print("The LinkedList Is Empty")
            return
        itr = self.head
        charRight = ""
        charLeft = ""
        while itr :
            charRight+= itr.data+"==>" if itr.next else itr.data
            if itr.next is None :
                tail = itr
            itr = itr.next
        #reverse
        itr = tail
        while itr :
            charLeft+=itr.data+"<==" if itr.prev else itr.data
            itr = itr.prev
        print(charRight)
        print(charLeft)
    
if __name__ == "__main__":
    ll = Linkedlist()
    ll.add_at_beg("1")
    ll.add_at_beg("2")
    ll.add_at_beg("3")
    ll.add_at_beg("4")
    ll.add_at_beg("5")
    ll.add_at_beg("6")
    ll.add_at_beg("7")
    ll.add_to_end("8")
    ll.delete_by_value("2")
    ll.insert_after_val("10","5")
    ll.insert_before_val("4","5")
    ll.print()