# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find tail
        # get length of linked list
        # dp modulo on the len to find actual rotation
        # rotation

        if not head or not head.next:
            return head
            
        tail = head
        length = 1
  
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if (k == 0):
            return head

        curr = head

        for i in range(length - k - 1):
            curr = curr.next        

        new_head = curr.next
        curr.next = None
        tail.next = head

        return new_head