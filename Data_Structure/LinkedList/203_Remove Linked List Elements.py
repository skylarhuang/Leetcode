class Solution1:
    def removeElements(self, head, val):
#解决空链表
        if head == None:
            return head
#解决都删光        
        while head.val == val:
            head = head.next
            if head == None:
                return head
            
        fake_head = ListNode(None)
        fake_head.next = head
        pre, cur = fake_head, head
        while cur:
            if cur.val == val:
                prev.next, cur = cur.next, cur.next
            else:
                prev, cur = cur, cur.next
        return fake_head.next


class Solution2:
    def removeElements(self, head, val):
        new_head = ListNode(None)
        curr = new_head
        while head:
            if head.val == val:
                head = head.next
            else:
                curr.next = head
                curr, head = curr.next, head.next
        # 如果不加下一句，无法删除最后一个node
        curr.next = None
        return new_head.next

class Solution3:
       def removeElements3(self, head, val):
	new_head = ListNode(-1)
	curr = new_head
	while head:
		if head.val != val:
			new_node = ListNode(head.val)
			curr.next = new_node
			curr = curr.next
			head = head.next
		else:
			head = head.next
       return new_head.next