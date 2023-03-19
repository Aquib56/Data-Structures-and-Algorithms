class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
    def removeNthFromEnd(self, head, n):
        ptr=head
        ptr2=head
        lenght=0
        j=0
        if ptr.next:
            while ptr.next:
                ptr=ptr.next
                lenght+=1
            index=(lenght-n)+1
        if index==0:
            return head.next   
        while j!=index-1:
            if ptr2.next:
                ptr2=ptr2.next
                j+=1
        ptr2.next=ptr2.next.next
        return head

if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(1)
    l1_n2=ListNode(2)
    l1_n3=ListNode(3)
    l1_n4=ListNode(4)
    l1_n5=ListNode(5)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n5
    l1.printLL(l1.head)
    l1.printLL(l1.removeNthFromEnd(l1.head,5))
        