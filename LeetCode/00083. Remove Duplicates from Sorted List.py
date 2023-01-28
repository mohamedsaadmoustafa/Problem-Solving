# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        prev, current = head, head.next
        while prev and current:
            if prev.val == current.val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return head
