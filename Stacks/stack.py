from node import Node

class Stack:

	def __init__(self):
		self.head = None

	def push(self,data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node

		else:
			temp = self.head

			self.head = new_node
			new_node.next = temp

	def peek(self):
		temp = self.head

		return temp.data

	def pop(self):
		temp = self.head

		self.head = temp.next
		data = temp.data
		temp = None

		return data

	def is_empty(self):
		if self.head is None:
			return True
		return False

	def print_stack(self):
		temp = self.head

		while(temp is not None):
			print(temp.data)
			temp = temp.next