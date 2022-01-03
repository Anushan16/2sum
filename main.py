def twoSum(nums,target):
  for i in range(len(nums)):
    for k in range(i+1,len(nums)):
      if nums[i] + nums[k] == target:
        return (i,k)
  else:
    return("target is not a sum of any two numbers in the list provided")


print(twoSum([2,4,6],11))