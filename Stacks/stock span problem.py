from stack import Stack

if __name__ == '__main__':

	stack = Stack()

	stocks = [100, 80, 60, 70, 60, 75, 85]

	s = [1] * len(stocks)

	s[0] = 1
	stack.push(0)

	for i in range(1, len(stocks)):
		while(not stack.is_empty() and stocks[i] > stocks[stack.peek()]):
		    stack.pop()

		s[i] = (i + 1) if stack.is_empty() else  (i - stack.peek())
		stack.push(i)

	print(s)