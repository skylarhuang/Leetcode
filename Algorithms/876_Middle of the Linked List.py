class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        len = 0
        while node.next:
            node = node.next
            len += 1
        mid = math.ceil(len / 2)
        node = head
        for i in range(mid):
            node = node.next
        return node

## New Method, Fast Slow Pointer, Save Space complexity to O(1)?
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow