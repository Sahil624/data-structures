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

	def delete_specific(self,key):
		# Store head node
		temp = self.head
		key = int(key)
 		
		if temp is None:
			print("Nodne\n")

        # If head node itself holds the key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
		while(temp is not None):
			if (temp.data == key):
				break
			prev = temp
			temp = temp.next
 
        # if key was not present in linked list
		if(temp == None):
			return
 
        # Unlink the node from linked list
		prev.next = temp.next
 
		temp = None

	def delete_this_node(self,key,no):
		temp = self.head

		if temp is None:
			print("List Is Empty")
			return

		if (key == 0):
			self.head = temp.next
			temp = None

		for i in range(0,key-1):
			temp = temp.next
			if temp is None:
				break

		if temp is None:
			return

		if (temp.next is None):
			return

		next = temp.next.next
 
        # Unlink the node from linked list
		temp.next = None
 
		temp.next = next

	def length(self):
		temp = self.head

		if temp is None:
			print("List is Empty")
			return 0

		i = 0 

		while(temp is not None):
			temp = temp.next
			i = i + 1

		return i