test = int(input())

for j in range(0,test):
	
	cows = input()
	pp = cows.split(' ')
	# print(pp)
	cows = int(pp[1])
	# no = int(input())
	no = int(pp[0])
	
	
	stalls = []
	
	for i in range(0,no):
		stalls.append(int(input()))
	
	stalls = sorted(stalls)
	
	dis =999999
	
	max_dis = no/(cows)

	max_dis = int(max_dis)

	max_dis=max_dis+1
	print(max_dis)
	cows=cows-2
	for i in range(0,no-max_dis,max_dis):
		cows=cows-1
		if cows < 0:
			break
		print(dis,(stalls[i+max_dis] - stalls[i]))
		if(dis>(stalls[i+max_dis] - stalls[i])):
			dis = stalls[i+max_dis] - stalls[i]
	
	print(dis)


# 1        
# 5 3
# 1
# 3
# 4
# 8
# 9
