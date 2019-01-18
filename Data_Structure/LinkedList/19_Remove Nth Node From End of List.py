class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
    
        index = length - n
        newhead = ListNode(None)
        newhead.next = head
        curr = newhead
        while index != 0:
            curr = curr.next
            index -= 1
    
        if curr.next:
            curr.next = curr.next.next
        else:
            return newhead.next
        
        return newhead.next