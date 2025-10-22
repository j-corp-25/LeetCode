# Last updated: 10/22/2025, 12:09:51 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = deque()
        count = 0
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next
            count +=1 
        
        curr = head
        for i in range(count // 2):
            last_node = stack.pop()
            last_node.next = curr.next
            curr.next = last_node
            curr = curr.next.next

        curr.next = None
        