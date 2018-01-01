from node import Node

class Linked_list:
	# Constructor
	def __init__(self):
		self.head = None

	# Printing List
	def print_list(self):
		temp = self.head

		while(temp):
			print(temp.data)
			temp = temp.next

	# Inserting at Starting
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Inserting After Specific Node
	def insert_after(self,prev,new_data):

		if prev is None:
			print("Node not in Linked List\n")

		new_node = Node(new_data)

		new_node.next = prev.next
		prev.next = new_node

	# Inserting At Last of Linked list
	def append(self,new_data):
		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head

		while(last.next):
			last = last.next

		last.next = new_node