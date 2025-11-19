import sys


def rob(nums):
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # dp array
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[-1]


def main():
    data = sys.stdin.read().strip()
    if not data:
        print(0)
        return

    nums = list(map(int, data.split()))
    print(rob(nums))


if __name__ == "__main__":
    main()
