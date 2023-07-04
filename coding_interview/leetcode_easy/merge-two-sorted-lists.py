# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start_ptr = ListNode()
        cur_ptr = start_ptr
        ptr1 = list1
        ptr2 = list2

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                cur_ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                cur_ptr.next = ptr2
                ptr2 = ptr2.next
            cur_ptr = cur_ptr.next
        
        if ptr1 is None:
            cur_ptr.next = ptr2
        elif ptr2 is None:
            cur_ptr.next = ptr1
        return start_ptr.next
        