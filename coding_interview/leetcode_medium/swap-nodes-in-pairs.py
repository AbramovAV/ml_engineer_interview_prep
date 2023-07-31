# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            ptr = head
            ptr_prev = None
            while ptr and ptr.next:
                buf = ptr.next.next
                ptr.next.next = ptr
                if not ptr_prev:
                    head = ptr.next
                else:
                    ptr_prev.next = ptr.next
                ptr.next = buf
                ptr_prev = ptr
                ptr = ptr.next
        return head