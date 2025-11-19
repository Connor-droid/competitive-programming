def count_above_median(nums):
    nums.sort()
    n = len(nums)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 1:
        median = nums[mid]
    else:
        median = (nums[mid - 1] + nums[mid]) / 2
    count = 0
    for x in nums:
        if x > median:
            count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
print(count_above_median(arr))