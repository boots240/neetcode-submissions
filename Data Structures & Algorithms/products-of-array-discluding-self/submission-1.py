class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *(len(nums))

        pre = 1
        for n in range(len(nums)):
            res[n] = pre 
            pre *= nums[n]

        post = 1
        for n in range(len(nums)-1 , -1, -1):
            res[n] *= post
            post *= nums[n]
        


        return res
        
            

            

        



        
            