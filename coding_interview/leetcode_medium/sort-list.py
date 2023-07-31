# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            ptr = head
            list_len = 0
            while ptr:
                ptr = ptr.next
                list_len += 1
            right_ptr = head
            prev_ptr = head
            for i in range(list_len//2 - 1):
                right_ptr = right_ptr.next

            prev_ptr = right_ptr
            right_ptr = right_ptr.next
            prev_ptr.next = None
            head = self.sortList(head)
            right_ptr = self.sortList(right_ptr)

            new_head = ListNode()
            ptr = new_head
            while head is not None and right_ptr is not None:
                if head.val < right_ptr.val:
                    ptr.next, head = head, head.next
                else:
                    ptr.next, right_ptr = right_ptr, right_ptr.next
                ptr = ptr.next
            
            if head is not None:
                ptr.next = head
            else:
                ptr.next = right_ptr
            return new_head.next