# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = ListNode(0)
        ans,temp = carry,0
        while l1 != None or l2 != None:
        	val = temp
        	if l1 != None:
        		val = val+l1.val
        		l1 = l1.next
        	if l2 != None:
        		val = val + l2.val
        		l2 = l2.next
        	temp = val//10
        	val = val%10
        	carry.next = ListNode(val)
        	carry = carry.next
        if temp == 1:
        	carry.next = ListNode(1)
        return ans.next



if __name__ == '__main__':
	p = ListNode(1)
	print(p.val)
	l1,l1.next,l1.next.next = ListNode(2),ListNode(4),ListNode(3)
	l2,l2.next,l2.next.next = ListNode(5),ListNode(6),ListNode(4)

	s = Solution()
	fff = s.addTwoNumbers(l1, l2)
	while fff != None:
		print(fff.val)
		fff = fff.next