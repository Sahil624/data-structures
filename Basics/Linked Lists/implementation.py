from node import Node
from linked_list import Linked_list as lil

if __name__ == '__main__':

	llist = lil()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third

	llist.print_list()