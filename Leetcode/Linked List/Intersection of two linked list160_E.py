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
    def getIntersectionNode(self, headA, headB):
        ptr1=headA
        ptr2=headB
        mapNodes={}
        while ptr1:
            mapNodes[ptr1]=ptr1
            ptr1=ptr1.next
        while ptr2.next is not None and ptr2 not in mapNodes:
            ptr2=ptr2.next
        if ptr2==None or ptr2.next==None:
            return None 
        else: 
            return ptr2.val
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         ptr1=headA
#         ptr2=headB
#         mapNodes={}
#         while ptr1:
#             mapNodes[ptr1]=ptr1
#             ptr1=ptr1.next
#         while ptr2.next or ptr2 not in mapNodes:
#             ptr2=ptr2.next
#         if ptr2==None or ptr2.next==None:
#              return None 
#         else: 
#             return ptr2
if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(1)
    # l1_n2=ListNode(2)
    # l1_n3=ListNode(3)
    # l1_n4=ListNode(4)
    # l1_n5=ListNode(5)
    # l1.head.next=l1_n2
    # l1_n2.next=l1_n3
    # l1_n3.next=l1_n4
    # l1_n4.next=l1_n5

    l2=LinkedList()
    l2.head=ListNode(1)
    # l2_n7=ListNode(7)
    # l2_n8=ListNode(8)
    # l2.head.next=l2_n7
    # l2_n7.next=l2_n8
    l1.printLL(l2.head)
    l1.printLL(l1.head)
    print(l1.getIntersectionNode(l1.head,l2.head))
