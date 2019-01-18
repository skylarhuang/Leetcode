    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(None)
        values = []
        curr = newhead
        while head:
            if head.val not in values:
                values.append(head.val)
                newnode = ListNode(head.val)
                curr.next = newnode
                curr = curr.next
            else:
                head = head.next
        return newhead.next