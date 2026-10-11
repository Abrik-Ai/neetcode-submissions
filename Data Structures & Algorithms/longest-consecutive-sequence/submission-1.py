class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        cons = 0
        for x in seen:
            if x - 1 not in seen:
                length = 1
                while x + length in seen:
                    length += 1
                cons = max(cons, length)
        return cons