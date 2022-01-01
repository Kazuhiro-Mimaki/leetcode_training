# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next