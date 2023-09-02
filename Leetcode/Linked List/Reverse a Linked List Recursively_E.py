class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
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
    def reverseList(self, head):
        prev=None
        def helper(curr,prev):
            if curr==None:
                return prev
            nxt=curr.next
            curr.next=prev
            prev=curr
            return helper(nxt,prev)
        return helper(head,prev)

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
    print(l1.printLL(l1.reverseList(l1.head)))


