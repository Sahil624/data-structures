from node import Node
from linked_list import Linked_list as lil

if __name__ == '__main__':

	no = int(input("Enter Number of nodes in Linked list\n"))
	n = no

	llist = lil()
	while no != 0:
		inp = input("Enter item number {}\n".format(n-no))
		llist.push(inp)
		no = no - 1

	key = int(input("Enter the no of node to delete\n"))

	llist.delete_this_node(key,n)

	print("After Deleting The Node\n")
	llist.print_list()