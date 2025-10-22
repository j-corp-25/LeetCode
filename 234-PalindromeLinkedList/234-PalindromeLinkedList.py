# Last updated: 10/22/2025, 12:09:43 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        myList = []
        while head:
            myList.append(head.val)
            head = head.next
        
        left = 0
        right = len(myList) - 1

        while left < right:
            if myList[left] == myList[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        