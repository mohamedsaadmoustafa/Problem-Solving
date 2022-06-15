class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next

class Solution:
    def __init__(self):
        self.head = None
    
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
