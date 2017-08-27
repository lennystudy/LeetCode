class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    length = 0
    if node is None:
    	return length
    while node is not None:
    	length += 1
    	node = node.next
    return length
def count(node,data):
    count = 0
    if node is None:
    	return count
    while node is not None:
    	if data == node.data:
    		count = count + 1
    	node = node.next
    return count

print(Node('99'))

print(length(Node('99')))

