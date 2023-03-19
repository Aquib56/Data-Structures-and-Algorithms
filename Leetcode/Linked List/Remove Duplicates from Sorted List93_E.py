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
class Solution(object):
    def DeleteDuplicates(self, head):
        ptr=head
        l=head
        r=head.next
        while(l):
            while(l.val!=r.val):
                r=r.next
            l.next=r.next
            r=r.next
            if(l==l.next):
                print(l.val,r.val)
                break
            else:
                l=l.next
        return head
    def deleteDuplicates(self,head):
        ptr=head
        while(ptr):
            while ptr.next and ptr.val==ptr.next.val:
                ptr.next=ptr.next.next
            ptr=ptr.next
        return head

if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(1)
    l1_n2=ListNode(1)
    l1_n3=ListNode(1)
    l1_n4=ListNode(3)
    l1_n5=ListNode(3)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n5
    e1=Solution()
    e1=e1.deleteDuplicates(l1.head)
    l1.printLL(e1)