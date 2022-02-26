# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            # 次のNodeをtempNextに保持しておく
            tempNext = curr.next
            # 前のNodeを次のNodeポインタにセット
            curr.next = prev
            # 現在のNodeを前のNodeとして保持しておく
            prev = curr
            # 保持していたtempNextを現在のNodeにセット
            curr = tempNext
        return prev
