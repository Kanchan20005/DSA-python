# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        initial = []
        while head:
            initial.append(head)
            head = head.next
            if not head:
                return False
            if head in initial:
                return True
        return False