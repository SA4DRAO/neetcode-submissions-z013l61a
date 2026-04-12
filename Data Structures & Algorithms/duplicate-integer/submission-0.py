class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = []
        for i in nums:
            if i in uniq:
                return True
            else:
                uniq.append(i)
        return False