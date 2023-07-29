class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        ptr=head
        ptr2=head
        count=0
        while ptr:
            ptr=ptr.next
            count+=1
        for i in range(count//2):
            head=head.next
        return head.data