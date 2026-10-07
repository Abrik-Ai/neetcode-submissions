class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums = {}
        for i in range(len(nums)):
            part = target - nums[i]
            if part in dnums:
                return [dnums[part], i]
            dnums[nums[i]] = i
            
