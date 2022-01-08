number = list(input())
nums = []
for i in number:
    nums.append(int(i))
# print(nums)
nums.sort(reverse=True)
for j in nums:
    print("%d" % j, end='')
