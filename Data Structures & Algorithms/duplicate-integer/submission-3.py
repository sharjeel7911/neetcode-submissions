# Sept 28, 2026
# TC: O(n)
# SC: O(n)
# hash-set
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False