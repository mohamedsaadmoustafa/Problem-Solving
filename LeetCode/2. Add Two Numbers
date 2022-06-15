# Without using linkedlist
class Solution:    
    def __expand(self, array, n):
        return array + [0]*n

    def addTwoNumbers(self, l1, l2):
        values = []
        carry = 0
        n1, n2 = len(l1), len(l2)
        diffrence = n1 - n2
        if diffrence > 0: l2 = self.__expand(l2, diffrence)
        if diffrence < 0: l1 = self.__expand(l1, -diffrence)

        for i, value in enumerate(l1):
            sum_ = value + l2[i] + carry
            print(f"#{i} {sum_}")
            if sum_ > 9:
                sum_ -= 10
                carry = 1
            else:
                carry = 0
            values.append(sum_)
        return values
        
        
# With using linkedlist
class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, result = None, None
        carry = 0
        while l1 or l2:
            l1_item = l1.val if l1 else 0
            l2_item = l2.val if l2 else 0
            sum_ = l1_item + l2_item + carry
            carry = 1 if sum_ > 9 else 0
            node = ListNode(sum_ % 10)
            
            if head: head.next = head = node
            else:    head = result = node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry: head.next = ListNode(1)
        return result
