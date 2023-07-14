# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        while ptr1.next:
            if n:
                n -= 1
            else:
                ptr2 = ptr2.next
            ptr1 = ptr1.next
        if n>0:
            return ptr2.next
        else:
            ptr2.next = ptr2.next.next
        return head