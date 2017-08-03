# Definition for singly-linked List.
# class ListNode:
#       def __init__(self, x):
#           self.val = x
#           self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        # write your code here
        newhead=ListNode(0); newhead.next = start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]

    def reverseKGroup(self, head, k):
        if head==None: return None
        nhead=ListNode(0); nhead.next=head; start=nhead
        while start.next:
            end= start
            for i in range(k-1):
                end = end.next
                if end.next == None:return nhead.next
            res=self.reverse(start.next, end.next)
            start.next= res[0]
            start= res[1]
    return nhead.next
