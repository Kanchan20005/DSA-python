# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is  None and list2 is None:
            return None
        finalList = ListNode()
        Head = ListNode()
        a = list1
        b = list2
        
        while a is not None or b is not None:
            if a is None and b is not None:
                if Head.val == 0 and Head.next is None:
                    Head.val = b.val
                    finalList = Head
                finalList.val = b.val
                b = b.next
                if  b is not None:
                    finalList.next = ListNode()
                finalList = finalList.next
            elif b is None and a is not None :
                if Head.val == 0 and Head.next is None and a.val is not 0:
                    Head.val = a.val
                    finalList = Head
                finalList.val = a.val
                a = a.next
                if  a is not None:
                    finalList.next = ListNode()
                finalList = finalList.next
            
            elif a is None and b is None:
                break

            elif a.val <= b.val:    
                if Head.val == 0 and Head.next is None and a.val is not 0:
                    Head.val = a.val
                    finalList = Head
                finalList.val = a.val
                a = a.next
                if a is not None or b is not None:
                    finalList.next = ListNode()
                finalList = finalList.next
            else:
                if Head.val == 0 and Head.next is None and b.val is not 0:
                    Head.val = b.val
                    finalList = Head
                    Head.next = ListNode()
                finalList.val = b.val
                b = b.next
                if a is not None or b is not None:
                    finalList.next = ListNode()
                finalList = finalList.next
        print(Head)
        return Head
