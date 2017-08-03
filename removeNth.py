class Solution(object):
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(0, n):
            head = head.next
        while head!=None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
    return res.next
