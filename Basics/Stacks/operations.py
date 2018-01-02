from node import Node
from stack import Stack

if __name__ == '__main__':
	st = Stack()

	st.push(1)
	st.push(5)
	st.push(2)

	st.print_stack()

	print("Peek Operation",st.peek())

	print("Pop Operation",st.pop())
	st.print_stack()

	print("Is Empty",st.is_empty())