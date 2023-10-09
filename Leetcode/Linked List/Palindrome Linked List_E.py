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

    def isPalindrome(self, head):
        d={}
        p1=head
        p2=head
        i,j=0,0
        while p1:
            i+=1
            d[i]=p1.val
            p1=p1.next
        while p2 and i!=j:
            j+=1
            print(j,i-j)
            if d[j]!=d[i-j+1]:
                return False
        return True

if __name__=="__main__":
    s=Solution()
    l1=LinkedList()
    l1.head=ListNode(1)
    l1_n2=ListNode(2)
    l1_n3=ListNode(2)
    l1_n4=ListNode(1)
    # l1_n5=ListNode(5)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    l1_n3.next=l1_n4
    # l1_n4.next=l1_n5
    l1.printLL(l1.head)
    print(s.isPalindrome(l1.head))
        
        