class TreeNode(object):
	
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right


class Tree(object):
	"""docstring for Tree"""
	def __init__(self, root):
		print("init")
		self.root = root

	#前序遍历 根-左-右
	def preOrder(self, treenode):
		if treenode is None:
			return
		print(treenode.data)
		preOrder(treenode.left)
		preOrder(treenode.right)


if __name__ == '__main__':
	#初始化二叉树
	node = TreeNode(1,2,3)
	tree = Tree(2)
	tree.preOrder(node)

		
		