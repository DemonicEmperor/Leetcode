class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        for window_size in range(l, r + 1):
            window_sum = sum(nums[:window_size])
            if window_sum > 0:
                ans = min(ans, window_sum)

            for i in range(window_size, n):
                window_sum += nums[i] - nums[i - window_size]
                if window_sum > 0:
                    ans = min(ans, window_sum)

        return -1 if ans == float('inf') else ans
