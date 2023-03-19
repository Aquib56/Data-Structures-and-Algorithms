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
    def swapPairs(self, head):
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr and curr.next:
            nextPair=curr.next.next
            second=curr.next

            second.next=curr
            curr.next=nextPair
            prev.next=second

            prev=curr
            curr=nextPair
        return dummy.next
if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(1)
    l1_n2=ListNode(2)
    l1_n3=ListNode(3)
    l1_n4=ListNode(4)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1.printLL(l1.head) 
    l1.printLL(l1.swapPairs(l1.head))