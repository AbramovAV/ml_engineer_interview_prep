# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra_one = 0
        summ = ListNode()
        ptr = summ
        while l1 or l2 or extra_one:
            ptr.next = ListNode()
            ptr = ptr.next
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            res = val1 + val2 + extra_one
            extra_one, res = res // 10, res % 10
            ptr.val = res
        return summ.next