class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n, i in enumerate(nums):
            complement = target - i
            if complement in seen:
                return [seen[complement], n]
            seen[i] = n
        return []