class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next

class Solution:
    def __init__(self):
        self.head = None
    
    def reverseList(self, head):
        #print(head.val)

        if not head or not head.next: return head
        x = self.reverseList(head.next)
        print(x.val)
        current = head.next
        current.next = head
        head.next = None
        return x
