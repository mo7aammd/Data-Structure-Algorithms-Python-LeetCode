# https://leetcode.com/problems/two-sum/
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap:
                n = hashmap[comp]
                if n != i:
                    return[i, n]
        return []