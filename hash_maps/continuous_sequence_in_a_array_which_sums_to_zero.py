class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, arr):
        hash_map = {}
        sums = 0
        
        for i in range(0,len(arr)):
            if sums in hash_map:
                print("returning",hash_map[sums],arr[hash_map[sums]:i])
         	return arr[hash_map[sums]:i]
            else:
                print("NONE",i,len(arr))
                if(i == len(arr)):
                    print("RETURN NONE")
                    return None
                else:
                    print("ADDING",sums,i)
                    hash_map.setdefault(sums,i)
                    sums += arr[i]
        print("END")
        return None
                    

if __name__ == "__main__":
	sol = Solution()
	arr = {1,2,-2,4,5}
	print(sol.lszero(arr)
