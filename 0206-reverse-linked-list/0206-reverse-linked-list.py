# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # queue = []
        first1 = head1 = ListNode()
        if not head:
            return head
        head1.val =first1.val =head.val
        head = head.next
        while head:
            first1 = ListNode()
            first1.val = head.val
            head = head.next
            first1.next = head1
            head1 = first1
        return first1

