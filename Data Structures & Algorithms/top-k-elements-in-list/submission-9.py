class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dnums = {}
        for num in nums:
                dnums[num] = dnums.get(num, 0) + 1

        keys = sorted(dnums.keys(), key=lambda n: dnums[n], reverse=True)
        return keys[:k]