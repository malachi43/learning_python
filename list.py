nums = [-100,0,1,2,3,4,5,6,7,8,9]
names = ["a","b","c","d","e","f"]
names.append("malachi")
nums.insert(0,"O")
nums.remove("O")
value = names.pop()
print("value: ",value)

current = names.pop(-3)
print("current: ",current)
combine = [nums, names]
numsNames = nums + names

print(nums)
print(names)
print(combine[0])
# print(combine[1][5])
print(numsNames)

nums.extend([10,11,12,13,14,15])
nums[9:11] = [13,17]
nums.reverse()
print(nums)
print("max: ", max(nums))
print("min: ", min(nums))
print("min names: ", min(names))
print("max names: ", max(names))
print("sum: ", sum(nums))

a = [33,76,24,56]
b = ["navin","kiran","harsh"]
print((a[:2] + b[1:])[-3])
