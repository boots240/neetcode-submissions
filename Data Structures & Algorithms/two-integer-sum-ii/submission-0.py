class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        r = len(numbers) - 1 
        l = 0

        num = 0

        while r > l:
            print(numbers[l],numbers[r])
            num = numbers[l] + numbers[r]
            
            if num > target:
                r -= 1
            elif num < target:
                l += 1
            else:
                return [l+1,r+1]


        