class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self,h):
        n=h
        if(n is None):
            print("Linked list is empty")
        else:
            while(n is not None):
                print(n.data,end="->")
                n=n.next
            print("None")

    def segregate(self, head):
        ptr=head
        ptr2=head
        zero,one,two=0,0,0
        while ptr:
            if ptr.data==0:
                zero+=1
            elif ptr.data==1:
                one+=1
            else:
                two+=1
            ptr=ptr.next
        dummy=head
        for i in range(zero):
            head.data=0
            if head.next:
                head=head.next
        for i in range(zero):
            head.data=1
            if head.next:
                head=head.next
        for i in range(zero):
            head.data=2
            if head.next:
                head=head.next
        return dummy

        



if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(1)
    l1_n2=Node(2)
    l1_n3=Node(2)
    l1_n4=Node(1)
    l1_n5=Node(2)
    l1_n6=Node(0)
    l1_n7=Node(2)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n5
    l1_n5.next=l1_n6
    l1_n6.next=l1_n7
    l1.printLL(l1.head)
    l1.printLL((l1.segregate(l1.head)))
