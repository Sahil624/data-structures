from stack import Stack

if __name__ == '__main__':

	st = Stack()

	expr = '10 2 + 6 *'

	arr = expr.split(' ')

	for i in arr:
		if ( ( i != '*' ) and ( i != '/') and ( i != '+' ) and ( i != '-') ):
			st.push(int(i))
			print('pushing',i)
		else:

			a = st.pop()
			b = st.pop()

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