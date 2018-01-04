# -3 14 18 -5 30 

from stack import Stack

def sort(st):
	if st.is_empty():
		return
	S = st.pop()

	sort(st)

	insert_items(st,S)

def insert_items(st,item):

	if not(st.is_empty()):
		if item < st.peek() :
			top = st.pop()
			st.push(item)
			st.push(top)

		else:
			st.push(item)

	else:
		st.push(item)

if __name__ == '__main__':
	st = Stack()

	arr = [-3 ,14 ,18 ,-5 ,30]

	for i  in arr:
		st.push(i)

	sort(st)

	st.print_stack()
