class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {v: i for i, v in enumerate(nums)}  # O(1) value → index lookup

        for index, value in enumerate(nums):
            need = target - value
            if need in nmap and nmap[need] != index:
                return [index, nmap[need]]