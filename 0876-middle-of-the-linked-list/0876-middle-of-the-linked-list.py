# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        i = 0
        while fast:
            i+=1
            fast = fast.next
            if i%2 == 0:
                slow = slow.next

        return slow