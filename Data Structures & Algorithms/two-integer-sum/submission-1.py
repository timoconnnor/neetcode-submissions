# nums = [3,4,5,6] target=7
# i=0 n=3. comp = 4. no 4 in dict, dict[3]=0
# i=1 n=4 comp = 3. Yes 3 in dict. retrun the 3 and our 4 indexes
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            complement = target - n

            if complement not in dict:
                dict[n] = i
            else:
                return [dict[complement], i]




        