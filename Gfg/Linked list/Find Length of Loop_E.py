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

    def countNodesinLoop(self,head):
        ptr=head
        count=0
        map={}
        while ptr:
            if ptr not in map:
                map[ptr]=1
            elif ptr in map and map[ptr]==1:
                map[ptr]+=1
                count+=1
            else:
                break
            ptr=ptr.next
        return count


if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(12)
    l1_n2=Node(15)
    l1_n3=Node(10)
    l1_n4=Node(11)
    l1_n5=Node(6)
    l1_n6=Node(2)
    l1_n7=Node(3)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n5
    l1_n5.next=l1_n6
    l1_n6.next=l1_n7
    l1_n7.next=l1_n3
    print(l1.countNodesinLoop(l1.head))
