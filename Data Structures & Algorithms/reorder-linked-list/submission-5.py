# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        node = slow.next
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        slow.next = None
        left = head
        right = prev

        while left and right:
            next_left = left.next
            left.next = right
            next_right = right.next
            right.next = next_left
            
            left = next_left
            right = next_right

        return None