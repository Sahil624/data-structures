from stack import Stack

def print_greater(st,arr):
	st.push(arr[0])

	for i in range(1,len(arr)):
		nex = arr[i]

		element = st.pop()

		while( element < nex ):
			print(str(element) + '------- ' + str(nex))

			if st.is_empty():
				break
			element = st.pop()

		if element > nex:
			st.push(element)

		st.push(nex)

	while (st.is_empty()  == False):
		element = st.pop()
		nex = - 1
		print(str(element) + '------- ' + str(nex))


if __name__ == '__main__':

	st = Stack()

	arr = [11, 13, 21, 3]

	print_greater(st,arr)