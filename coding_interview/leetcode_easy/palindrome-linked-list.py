# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head
        reversed_list = None
        tmp_ptr = slow_ptr
        step_back = False
        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            if fast_ptr:
                fast_ptr = fast_ptr.next
            else:
                step_back = True
            tmp_ptr.next = reversed_list
            reversed_list = tmp_ptr
            tmp_ptr = slow_ptr

        if step_back:
            reversed_list = reversed_list.next

        while reversed_list and slow_ptr:
            if slow_ptr.val != reversed_list.val:
                return False
            reversed_list = reversed_list.next
            slow_ptr = slow_ptr.next
        return True