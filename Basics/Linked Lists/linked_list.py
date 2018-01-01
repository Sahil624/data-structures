from node import Node

class Linked_list:
	def __init__(self):
		self.head = None

	def print_list(self):
		temp = self.head

		while(temp):
			print(temp.data)
			temp = temp.next

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insert_after(self,prev,new_data):

		if prev is None:
			print("Node not in Linked List\n")

		new_node = Node(new_data)

		new_node.next = prev.next
		prev.next = new_node