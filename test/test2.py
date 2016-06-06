# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


    def reserveList(self,head):
    	if head == None or head.next == None:
    		return head
    	cur = head
    	pre = None
    	res = head
    	print("begin")
    	while cur:
    		res = cur
    		tem = cur.next
    		cur.next = pre
    		pre = cur
    		cur = tem
    	print(head.next)
    	return res

if __name__ == '__main__':
	head = ListNode(5)
	print(head.val)
	tmp = ListNode(10)
	head.next = tmp
	temp1 = ListNode(15)
	tmp.next = temp1

	# while head:
	# 	print(head.val)
	# 	head = head.next


	print(head)
	#reserve list
	p = Solution()
	q = p.reserveList(head)
	while head:
		print(head.next)
		print(head.val)
		print("time")
		head = head.next

	while q:
		print(q.val)
		q = q.next
