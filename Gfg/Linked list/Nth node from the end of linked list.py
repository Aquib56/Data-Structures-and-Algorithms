class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self,h):
        n=h
        if(n is None):
            print("Linked list is empty")
        else:
            while(n is not None):
                print(n.val,end="->")
                n=n.next
            print("None")
    def getNthFromLast(self,head,n):
        ptr=head
        p=head
        count=0
        while ptr:
            ptr=ptr.next
            count+=1
        idx=count-n
        if idx<0:
            return -1
        i=0
        while i!=idx:
            p=p.next
            i+=1
        return p.val
    def getNthFromLast_better(self,head,n):
        ptr=head
        forward=head
        count=0
        while count!=n:
            if forward.next.next==None:
                return -1
            forward=forward.next
            count+=1
            
        while forward:
            forward=forward.next
            ptr=ptr.next
        return ptr.val


        



if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(1)
    l1_n2=Node(2)
    l1_n3=Node(3)
    l1_n4=Node(4)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1.printLL(l1.head)
    print((l1.getNthFromLast_better(l1.head,2)))
