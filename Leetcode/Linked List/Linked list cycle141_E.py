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

class Solution(object):
    def hasCycle(self, head):
        dict1={}
        ptr=head
        while(ptr):
            dict1[ptr]=1
            ptr=ptr.next
            if(ptr in dict1):
                return True
        return False
    def goated(self,head):
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(1)
    l1_n2=ListNode(2)
    l1_n3=ListNode(3)
    l1_n4=ListNode(4)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n2
    e1=Solution()
    print((e1.goated(l1.head)))