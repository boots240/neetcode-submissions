class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffhashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffhashmap:
                return [diffhashmap[diff], i ]
            diffhashmap[n] = i 
             
            
            
