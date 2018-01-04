from stack import Stack

def balanced(expr):

	st = Stack()

	for i in expr:
		if( (i == '(') or (i == '{') or (i == '[')):
			st.push(i)

		else:

			if( i == ')' ):
				if( (st.is_empty()) or (st.peek() != '(')):
					return False
				st.pop()

			elif(i == '}'):
				if( (st.is_empty()) or (st.peek() != '{')):
					return False
				st.pop()
			elif(i == ']'):
				if( (st.is_empty()) or (st.peek() != '[')):
					return False
				st.pop()

	if st.is_empty():
		return True
	return False

	return True

if __name__ == '__main__':

	xpr = "[({})]"

	if balanced(xpr):
		print("Balanced")

	else:
		print("Not Balanced")