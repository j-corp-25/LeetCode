# Last updated: 10/22/2025, 12:09:53 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myLinkSet = set()

        while head:
            if head in myLinkSet:
                return head
            else:
                myLinkSet.add(head)
                head = head.next
        
        