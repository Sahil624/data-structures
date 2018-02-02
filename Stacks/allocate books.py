# books = [73, 58, 30, 72, 44, 78, 23, 9]
# no = 5

books = [ 91, 20, 62, 33, 97, 31, 88, 89, 73, 77, 4, 58, 0, 54, 60, 15, 47, 80, 30, 55, 46, 7, 38, 0, 26, 35, 57, 13 ]
no = 24

# books = [ 31, 14, 19, 75 ]
# no = 12

# books = [12, 34, 67, 90]
# no = 2

total = 0

def binary_s(low,high):
	low = int(low)
	high = int(high)
	stds = [[]]
	stds[0] = []
	k = 0
	max_a = -9999
	mid = (low+high)/2
	print("MID",mid,low,high)
	if(mid >= high):
		return
	t = 0

	for i in books:
		t += i

		if (t<mid):
			stds[k].append(i)

		else:
			k += 1
			stds.append([])
			t = i
			stds[k].append(i)


	print(stds)
	if(len(stds) > no):
		# print("IGNORE THIS \\/ case")
		return binary_s(mid+1,high)

	elif(len(stds) < no):
		# print("IGNORE THIS \\/ case")
		return binary_s(low,mid)


	# binary_s(mid+1,high)

	else:
		for i in stds:
			su = 0
			for j in i:
				su += j
			if max_a < su:
				max_a = su
				# print(max_a

	return max_a

for i in books:
	total += i

if (len(books)>= no):
	mini = binary_s(0,total)
else:
	mini = -1
print(mini)