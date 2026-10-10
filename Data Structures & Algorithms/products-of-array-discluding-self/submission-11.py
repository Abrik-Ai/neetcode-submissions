class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        prod = 1
        for i in range(len(nums)):
            left.append(prod)
            prod *= nums[i]

        right = [1] * len(nums)
        prod = 1
        for j in range(len(nums) -1, -1, -1):
            right[j] = prod
            prod *= nums[j]

        output = []
        for i in range(len(nums)):                
            output.append(left[i] * right[i])
        return output 