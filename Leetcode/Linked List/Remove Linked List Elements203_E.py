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
    def RemoveElements(self, head, val):
        while head.val==val:
            if head.val==val:
                head=head.next
                print(head.val)      
        ptr=head
        print(ptr.val)
        while ptr.next!=None and ptr.next.next!=None:
            while (ptr.next).val!=val:
                ptr=ptr.next
            ptr.next=ptr.next.next
        return head      
    def removeElements(self, head, val):
        dummy=ListNode(next=head)
        prev,curr=dummy,head
        
        while curr:
            nxt=curr.next
            if curr.val==val:
                prev.next=nxt
            else:
                prev=curr
            curr=nxt
        return dummy.next
          
            
if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(6)
    l1_n2=ListNode(2)
    l1_n3=ListNode(6)
    l1_n4=ListNode(6)
    l1_n5=ListNode(5)
    l1_n6=ListNode(6)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n5
    l1_n5.next=l1_n6
    l1.printLL(l1.head)
    l1.printLL(l1.removeElements(l1.head,6))