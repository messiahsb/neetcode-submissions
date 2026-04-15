class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        count = {}
        for i in range(len(numbers)):
            
             if (target - numbers[i]) in count:
                return [count[target - numbers[i]]+1, i+1]
             
             count[numbers[i]] = i

        return []