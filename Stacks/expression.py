from stack import Stack

if __name__ == '__main__':

	st = Stack()

	expr = '2 3 1 * + 9 -'

	arr = expr.split(' ')

	for i in arr:
		if ( ( i != '*' ) and ( i != '/') and ( i != '+' ) and ( i != '-') ):
			st.push(int(i))
			print('pushing',i)
		else:

			b = st.pop()
			a = st.pop()

			print(a,b,i)

			if( i == '*'):

				st.push(a * b)

			elif( i == '/'):
				st.push(a / b)

			elif( i == '+'):
				st.push(a + b)

			elif( i == '-'):
				st.push(a - b)

	print(st.pop())