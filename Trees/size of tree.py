from tree import Tree

def size(root):
	if root is None:
		return 0

	else:
		return (size(root.left)+1+size(root.right))

if __name__=='__main__':
	root = Tree(1)
	root.left = Tree(2)
	root.right = Tree(3)
	root.left.left  = Tree(4)
	root.left.right = Tree(5)

	print(size(root))