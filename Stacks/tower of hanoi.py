from stack import Stack

def swap(source,destination):

	destination.push(source.pop())

def hanoi(no):
	moves = pow(2,no)
	# print("No of Moves required are ",moves)

	source = Stack()
	aux = Stack()
	dest = Stack()

	for i in range(0,no):
		source.push(no-i)

	source.print_stack()
	print('\n')

	for i in range(1,moves):
		# print(i % 3)

		if (i % 3 == 1):

			if not( source.is_empty() or dest.is_empty()):
				top1 = source.peek()
				top2 = dest.peek()
					
			if(source.is_empty()):
				swap(dest,source)

			elif(dest.is_empty()):
				swap(source,dest)

			elif(top1 > top2):
				swap(dest,source)

			elif(top2 > top1):
				swap(source,dest)

			else:
				print("Some thing went wrong in 1")


		elif( i % 3 == 2):

			if not( source.is_empty() or aux.is_empty()):
				top1 = source.peek()
				top2 = aux.peek()
					
			if(source.is_empty()):
				swap(aux,source)

			elif(aux.is_empty()):
				swap(source,aux)

			elif(top1 > top2):
				swap(aux,source)

			elif(top2 > top1):
				swap(source,aux)

			else:
				print("Some thing went wrong in 1")

		elif( i % 3 == 0):
			
			if not( aux.is_empty() or dest.is_empty()):
				top1 = aux.peek()
				top2 = dest.peek()
					
			if(aux.is_empty()):
				swap(dest,aux)

			elif(dest.is_empty()):
				swap(aux,dest)

			elif(top1 > top2):
				swap(dest,aux)

			elif(top2 > top1):
				swap(aux,dest)

			else:
				print("Some thing went wrong in 1")


	dest.print_stack()



if __name__ == '__main__':

	no_of_plates = 15


	hanoi(no_of_plates)