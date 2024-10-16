from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index_dict = {}
    
    for i, num in enumerate(nums):
        remain = target - num
        if remain in index_dict:
            return [index_dict[remain], i]
        index_dict[num] = i