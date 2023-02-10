class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = x = ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                x.next = list2
                list2 = list2.next
            else:
                x.next = list1
                list1 = list1.next
            x = x.next

        x.next = list1 or list2
        return head.next
