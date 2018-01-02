from node import Node
from linked_list import Linked_list as lil

if __name__ == '__main__':
	llist = lil()
	llist.push(7)
	llist.push(1)
	llist.push(3)
	llist.push(2)

	print("List before deletion\n")

	llist.print_list()

	key = input("Enter the key to be deleted\n")

	llist.delete_specific(key)

	print("After Deletion\n")

	llist.print_list()