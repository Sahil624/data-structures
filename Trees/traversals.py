from tree import Tree

def inorder(root):

	if root:
		inorder(root.left)
		print(root.val,end=' ')
		inorder(root.right)

def post(root):

	if root:
		post(root.left)
		post(root.right)
		print(root.val,end=" ")

def pre(root):

	if root:
		print(root.val,end=" ")
		pre(root.left)
		pre(root.right)

if __name__ == '__main__':

	root = Tree(1)
	root.left      = Tree(2)
	root.right     = Tree(3)
	root.left.left  = Tree(4)
	root.left.right  = Tree(5)

	inorder(root)
	print("")
	post(root)
	print("")
	pre(root)

