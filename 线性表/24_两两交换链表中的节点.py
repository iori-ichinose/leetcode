# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # recursion
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pnext = head.next
        head.next = self.swapPairs(pnext.next)
        pnext.next = head
        return pnext

    # normal
    def swapPairs_2(self, head: ListNode) -> ListNode:
        p = ListNode()
        p.next = head
        tmp = p
        while tmp.next and tmp.next.next:
            p1 = tmp.next
            p2 = tmp.next.next
            tmp.next = p2
            p1.next = p2.next
            p2.next = p1
            tmp = p1
        return p.next
