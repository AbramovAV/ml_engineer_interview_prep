# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        if stack:
            head = stack.pop()
        ptr = head

        while stack:
            ptr.next = stack.pop()
            ptr = ptr.next
        if head:
            ptr.next = None
        return head