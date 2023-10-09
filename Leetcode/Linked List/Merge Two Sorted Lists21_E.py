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
    def mergeTwoLists(self, list1, list2):
        bruh=ListNode()
        list3=bruh
        while list1 and list2:
            if list1.val<list2.val:
                list3.next=list1
                list1=list1.next
            else:
                list3.next=list2
                list2=list2.next
            list3=list3.next
        if list1:
            list3.next=list1
        elif list2:
            list3.next=list2        
        return bruh.next  
    
if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(1)
    l1_n2=ListNode(2)
    l1_n3=ListNode(4)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3

    l2=LinkedList()
    l2.head=ListNode(1)
    l2_n2=ListNode(2)
    l2_n3=ListNode(5)
    l2.head.next=l2_n2
    l2_n2.next=l2_n3
    e1=Solution()
    l2.printLL(e1.mergeTwoLists(l1.head,l2.head))
    
    
    


    