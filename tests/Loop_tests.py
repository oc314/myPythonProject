nums = [3, 3, 4, 5, 5, 5, 7, 7, 7, 1, 1, 1, 7, 5]
nums.sort()
for i in range(len(nums) - 1, 0, -1):
    if nums[i] == nums[i-1]:
        del nums[i]
print(nums)


prices = [1, 2, 3, 4, 5]
profit = 0
for i in range(len(prices) - 1):
    if prices[i] < prices[i+1]:
        profit = profit + prices[i+1] - prices[i]
        i += 2
print (profit)

nums = [1, 2, 3, 4, 5, 6, 7]
current_num = 0
k = 1
while k <= 3:
    current_num = nums[len(nums) - 1]
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i-1]
    nums[0] = current_num
    k += 1
print (nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
nums.reverse()
nums = nums[k-1::-1] + nums[:k-1:-1]
print (nums)


for n in range(10):
    if n % 2 == 0:
        print (n)

for n in range(10):
    if n % 2 != 0:
        print (n)


friends = ["Dimon", "Dimka", "Serega"]
for friend in friends:
    print("\n")
    for character in friend:
        print(character)
print(len(friends))
print("\nDone!")
