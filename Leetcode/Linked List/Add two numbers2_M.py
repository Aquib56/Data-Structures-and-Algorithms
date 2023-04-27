class ListNode(object):
    def __init__(self, x=0,next=None):
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
    # def addTwoNumbers(self, l1, l2,l3):
    #     updated=l3
    #     ptr1,ptr2=l1,l2
    #     count1,count2,n,count3=0,0,1,0
    #     while ptr1:
    #         count1+=n*ptr1.val
    #         n=n*10
    #         ptr1=ptr1.next
    #     n=1
    #     while ptr2:
    #         count2+=n*ptr2.val
    #         ptr2=ptr2.next
    #         n=n*10
        
    #     count3=count1+count2
    #     reversed_num = 0
    #     while count3!= 0:
    #         digit = count3 % 10
    #         reversed_num = reversed_num * 10 + digit
    #         count3 //= 10 
    #     str1=str(reversed_num)
    #     print(str1)
    #     i=0
    #     while i<len(str1):
    #         x=int(str1[i])
    #         print(x)
    #         updated.val=x
    #         updated=updated.next
    #         i+=1
            
    #     return l3
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        updated=dummy
        ptr1,ptr2=l1,l2
        count1,count2,n,count3=0,0,1,0
        while ptr1:
            count1+=n*ptr1.val
            n=n*10
            ptr1=ptr1.next
        n=1
        while ptr2:
            count2+=n*ptr2.val
            ptr2=ptr2.next
            n=n*10
        count3=count1+count2
        string=str(count3)
        str1 = string [::-1]
        i=0
        print(str1)
        while i<len(str1):
            x=int(str1[i])
            updated.next=ListNode(x)
            updated=updated.next
            i+=1
        return dummy.next
    
    def addTwoNumbers123(self, l1, l2):
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while l1 and l2:
            sum=l1.val+l2.val+carry
            if sum>9:
              sum=sum%10
              curr.next=ListNode(sum)
              curr=curr.next
              carry=1
            else:
                curr.next=ListNode(sum)
                curr=curr.next
                carry=0
            l1=l1.next
            l2=l2.next
        while l1:
            curr.next=ListNode(l1.val)
            curr=curr.next
            l1=l1.next
        while l2:
            curr.next=ListNode(l2.val)
            curr=curr.next
            l2=l2.next
        return dummy.next 
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        updated=dummy
        ptr1,ptr2=l1,l2
        count1,count2,n,count3=0,0,1,0
        while ptr1:
            count1+=n*ptr1.val
            n=n*10
            ptr1=ptr1.next
        n=1
        while ptr2:
            count2+=n*ptr2.val
            ptr2=ptr2.next
            n=n*10
        
        count3=count1+count2
        reversed_num = 0
        while count3!= 0:
            digit = count3 % 10
            reversed_num = reversed_num * 10 + digit
            count3 //= 10 
        str1=str(reversed_num)
        print(str1)
        i=0
        while i<len(str1):
            x=int(str1[i])
            updated.next=ListNode(x)
            print(updated.val)
            updated=updated.next
            i+=1
        n=dummy
        if(n is None):
            print("Linked list is empty")
        else:
            while(n is not None):
                print(n.val,end="->")
                n=n.next
            print("None")
        return l3
                   

if __name__=="__main__":
    l1=LinkedList()
    l1.head=ListNode(2)
    l1_n2=ListNode(4)
    l1_n3=ListNode(3)
    l1.head.next=l1_n2
    l1_n2.next=l1_n3
    

    l2=LinkedList()
    l2.head=ListNode(5)
    l2_n7=ListNode(6)
    l2_n8=ListNode(4)
    l2.head.next=l2_n7
    l2_n7.next=l2_n8
    l1.printLL(l2.head)
    l1.printLL(l1.head)
    l1.printLL(l1.addTwoNumbers123(l1.head,l2.head))

    l3=LinkedList()
    l3.head=ListNode(1)
    l3_n2=ListNode(1)
    l3_n3=ListNode(3)
    l3.head.next=l3_n2
    l3_n2.next=l3_n3
