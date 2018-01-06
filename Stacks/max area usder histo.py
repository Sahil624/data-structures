from stack import Stack

if __name__ == '__main__':

	hist = [ 6, 2, 5, 4, 5, 1, 6 ]

	st = Stack()

	area = -99
	max_area = -99
	i = 0

	while(i<len(hist)):
		if((st.is_empty()) or (hist[st.peek()] < hist[i])):
			st.push(i)
			i += 1


		else:
			top = st.pop()

			if(st.is_empty()):
				area = hist[top] * i

			else:
				area = hist[top] * (i - st.peek() - 1)


			if (area> max_area):
				max_area = area


	while((st.is_empty()) == False):
		top = st.pop()

		if(st.is_empty()):
			area = hist[top] * i

		else:
			area = hist[top] * (i - st.peek() - 1)


		if (area> max_area):
			max_area = area


	print(max_area)