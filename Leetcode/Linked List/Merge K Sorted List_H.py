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
    def merge(self,l1,l2):
        l=ListNode(0)
        dummy=l
        print(5)
        while l1 and l2:
            if l1.val >l2.val:
                dummy.next=l2
                l2=l2.next
            elif l2.val>l1.val:
                dummy.next=l1
                l1=l1.next
            dummy=dummy.next
        while l1:
            dummy.next=l1
            l1=l1.next
        while l2:
            dummy.next=l2
            l2=l2.next
        return l.next
    def mergeKLists(self, lists):
        if len(lists)>=2:
            mergedList=self.merge(lists[0],lists[1])
            for i in range(2,len(lists)):
                mergedList=self.merge(mergedList,lists[i])
            return mergedList
        return []
    def mergeKLists_better(self, lists):
        if len(lists)==0 or not lists:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(self.merge(l1,l2))
            lists=mergedList
        return lists[0]

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
    l2.printLL(e1.mergeKLists([l1.head,l2.head]))
    