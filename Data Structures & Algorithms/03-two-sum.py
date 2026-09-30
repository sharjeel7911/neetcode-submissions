# Sept 28, 2026
# TC: O(n)
# SC: O(n)
# hash-map
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for idx, val in enumerate(nums):
            first = val
            second = target - first

            if second in seen:
                return [seen[second], idx]
            else:
                seen[val] = idx
        return []
