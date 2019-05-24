def arrayPairSum(nums) -> int:
    sum_of_min = 0
    exists = [0]*2*10005
    for i in nums:
        exists[i + 10000] += 1
    odd = True
    for key, val in enumerate(exists):
        while val > 0:
            if odd:
                sum_of_min = sum_of_min + key - 10000
            odd = not odd
            val = val - 1
    return sum_of_min
    
print (arrayPairSum([1,4,3,2]))
print (arrayPairSum([1,4]))
print (arrayPairSum([6214, -2290, 2833, -7908])) #-5075