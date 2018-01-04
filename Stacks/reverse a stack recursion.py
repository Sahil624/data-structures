from stack import Stack

def reverse(st):

	if st.is_empty():
		return

	top = st.pop()
	reverse(st)
	st.push(top)

if __name__ == '__main__':
	st = Stack()

	arr = [-3 ,14 ,18 ,-5 ,30]

	for i  in arr:
		st.push(i)


	reverse(st)

	st.print_stack()