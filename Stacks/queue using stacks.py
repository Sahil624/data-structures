from stack import Stack

if __name__ == '__main__':

	st1 = Stack()
	st2 = Stack()

	inp = int(input("Enter 1 to push \nEnter 2 to pop\nEnter 9 to Exit\n"))

	while(inp != 9 ):

		if(inp == 1):
			val = int(input("Enter Value to be pushed\n"))
			st1.push(val)

		elif(inp == 2):
			if(st1.is_empty() and st2.is_empty()):
				print("Error")
				break
			else:
				if(st2.is_empty()):
					while(not(st1.is_empty())):
						popo = st1.pop()
						# print("Pushing",popo,'\n')
						st2.push(popo)
					print("Front is",st2.pop())

		inp = int(input("\n\nEnter 1 to push\nEnter 2 to pop\nEnter 9 to Exit\n\n"))



