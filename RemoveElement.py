class Solution:
    """
    @param A: A list integers
    @param elem: A integers
    @return : The new length after remove
    """
    def removeElement(self, A, elem):
        j= len(A)-1
        for i in range(len(A) -1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
    return j+1
