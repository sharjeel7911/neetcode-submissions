# Sept 28, 2026
# TC: O(n)
# SC: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums):
            first = val
            second = target - first 

            if second in seen:
                return [seen[second], idx]
            else:
                seen[val] = idx 