class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()

        out = []
        

        for e,i in enumerate(nums):
            right = len(nums)-1;
            left = e+1
            if e > 0 and i == nums[e - 1]:
                continue
            while left < right:
                if nums[left] + nums[right] > -i:
                    right-=1
                elif nums[left] + nums[right] < -i:
                    left+=1
                elif nums[left] + nums[right] == -i:
                    out.append([i, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                
                    
                    
        return out
