from tree import Tree

def depth(root):
	if root is None:
		return 0

	else:
		ldep = depth(root.left)
		rdep = depth(root.right)

		if(ldep > rdep):
			return ldep+1
		return rdep+1

if __name__ == '__main__':
	root = Tree(1)
	root.left = Tree(2)
	root.right = Tree(3)
	root.left.left  = Tree(4)
	root.left.right = Tree(5)

	print(depth(root))