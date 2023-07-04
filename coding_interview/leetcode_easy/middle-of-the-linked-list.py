# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_nodes = 0
        ptr = head
        while ptr:
            num_nodes += 1
            ptr = ptr.next
        ptr = head
        mid_node = num_nodes // 2
        for i in range(mid_node):
            ptr = ptr.next
        return ptr