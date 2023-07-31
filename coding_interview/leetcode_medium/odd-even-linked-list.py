# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd_head = head
            if head.next:
                even_head = head.next

                odd_ptr = odd_head
                even_ptr = even_head
                ptr = even_ptr.next
                idx = 3
                while ptr:
                    if idx % 2:
                        odd_ptr.next = ptr
                        odd_ptr = odd_ptr.next
                    else:
                        even_ptr.next = ptr
                        even_ptr = even_ptr.next
                    ptr = ptr.next
                    idx += 1
                odd_ptr.next = even_head
                even_ptr.next = None

            return odd_head