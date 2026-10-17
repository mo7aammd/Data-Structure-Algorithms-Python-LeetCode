def containsDuplicate(self, nums: list[int]) -> bool:
    sett = set(nums)
    if len(sett) == len(nums):
        return False
    return True