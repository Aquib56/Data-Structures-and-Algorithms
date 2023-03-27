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
    def removeLoop(self, head):
        slow,fast,start=head,head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if(fast==slow):
                ptr=fast
                break
        if fast is None or fast.next is None:
            return 0
        while ptr!=start:
            ptr=ptr.next
            start=start.next
        ptr=slow.next
        while(ptr.next!=start):
            ptr=ptr.next
        ptr.next=None
        return 1

# class Solution:
#     def removeLoop(self, head):
#         slow,fast,start=head,head,head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#             if(fast==slow):
#                 ptr=fast
#                 break
#         while ptr!=start:
#             ptr=ptr.next
#             start=start.next
#         ptr=slow.next
#         while(ptr.next!=start):
#             ptr=ptr.next
#         ptr.next=None
            
        
if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(1)
    l1_n2=Node(2)
    l1_n3=Node(3)
    l1_n4=Node(4)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    l1_n4.next=l1_n3
    l1.removeLoop(l1.head)
    l1.printLL(l1.head)
    # print((e1.removeLoop(l1.head)))