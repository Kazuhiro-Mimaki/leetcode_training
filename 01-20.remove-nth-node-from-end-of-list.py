# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return
        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next
        target_node_id = count - n
        if target_node_id == 0:
            return head.next
        id = 0
        dummy = head
        while dummy:
            id += 1
            if id == target_node_id:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return head
