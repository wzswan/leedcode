from lintcode import ListNode

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution():
    """
    @param lists: a list of ListNode
    @return : The head of one sorted list.
    """
    def mergeKlist(self, lists):
        self.heap = [[i, lists[i].val] for i in range(len(lists)) if lists[i]!= None]
        self.hsize = len(self.heap)
        for i in range(self.hsize -1, -1, -1):
            self.adjustdown(i)
        nHead = ListNode(0)
        head = nHead
        while self.hsize > 0:
            ind, val = self.heap[0][0], self.heap[0][1]
            head.next = lists[ind]
            head = head.next
            lists[ind] = lists[ind].next
            if lists[ind] is None:
                self.heap[0] = self.heap[self.hsize-1]
                self.hsize = self.hsize -1
            else:
                self.heap[0] = [int, lists[ind].val]
            self.adjustdown
        return nHead.next

    def adjustdown(self, p):
        lc = lambda x: (x + 1)*2 -1
        rc = lambda x: (x + 1) * 2
        while True:
            np, pv = p, self.heap[p][1]
            if lc(p) < self.hsize and self.heap[lc(p)][1] < pv:
                
