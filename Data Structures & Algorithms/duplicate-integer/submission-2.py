# Sept 28, 2026
# TC: O(n)
# SC: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if(i in seen):
                return True
            else:
                seen.add(i)
        return False            