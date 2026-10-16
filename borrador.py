class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j+1] == target:
                    
                    return objectivo

print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([3,2,4],6))