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
    def removeDuplicates(self, head):
        map={}
        back=head
        front=head.next
        map[back.val]=1
        while front:
            if front.val not in map:
                map[front.val]=1
                front=front.next
                back=back.next                
            elif front.val in map:
                back.next=front.next
                front=front.next
            else:
                front=front.next
                back=back.next
        return head

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(1)
    l1_n2=Node(2)
    l1_n3=Node(2)
    l1_n4=Node(2)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1.printLL(l1.head)
    l1.printLL(l1.removeDuplicates(l1.head))
