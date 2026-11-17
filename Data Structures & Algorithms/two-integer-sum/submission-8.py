class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i, nums in enumerate (nums):
            diff = target - nums 
            if diff in Map:
                return [Map[diff], i]
            Map[nums] = i
            