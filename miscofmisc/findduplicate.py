def findDup(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True
        
print(findDup([3,1,3,4,2]))