from tree import Tree

def push(root,key):
	if root is None:
		return Tree(key)

	if(key < root.val):
		root.left = push(root.left,key)

	elif(key > root.val):
		root.right = push(root.right,key)

	return root

def inorder(root):

	if root:
		inorder(root.left)
		print(root.val,end=' ')
		inorder(root.right)

if __name__ == '__main__':
	vals = [10, 5, 1, 7, 40, 50]

	root = Tree(vals[0])

	for i in vals[1:]:
		push(root,i)

	inorder(root)