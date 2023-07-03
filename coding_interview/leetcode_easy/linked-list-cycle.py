# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr_slow = head
        ptr_fast = head
        while ptr_slow is not None and ptr_fast is not None:
            if ptr_slow.next is None:
                return False
            elif ptr_fast.next is None or ptr_fast.next.next is None:
                return False
            ptr_slow = ptr_slow.next
            ptr_fast = ptr_fast.next.next
            if ptr_slow == ptr_fast:
                return True