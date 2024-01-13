user_input = input(
    "Enter numbs separated by space to find their average: ").split()
nums = list(map(int, user_input))
avg, sum = 0, 0

for i in range(len(nums)):
    sum += nums[i]

avg = sum/len(nums)

print(f"\nSum of observation = {sum}")
print(f"Number of observation = {len(nums)}")
print(f"Average = {sum}/{len(nums)}")
print(f"Average = {avg:.2f}\n")
