class Linked_list:
	def __init__(self):
		self.head = None

	def print_list(self):
		temp = self.head

		while(temp):
			print(temp.data)
			temp = temp.next