class solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
    
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        count = 0
        for i in range(n - 1):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n - 1] - left_sum
            if left_sum >= right_sum:
                count += 1

        return count

# Example usage:
if __name__ == "__main__":
    nums = [10, 4, -8, 3]
    sol = solution()
    print(sol.waysToSplitArray(nums))  # Output: 2