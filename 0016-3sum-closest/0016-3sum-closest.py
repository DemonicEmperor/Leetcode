class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                tot = nums[i]+nums[left]+nums[right]
                if abs(target-tot)<abs(res-target):
                    res = tot

                if tot==target:
                    return tot
                elif tot<target:
                    left+=1
                else:
                    right-=1
        return res
