from stack import Stack

def reverse(string):
	st = Stack()

	for i in string:
		st.push(i)

	new_string = ''

	while(not(st.is_empty())):
		new_string+=st.pop()

	return new_string

if __name__ == '__main__':

	string = 'revrse'

	string = reverse(string)

	print(string)