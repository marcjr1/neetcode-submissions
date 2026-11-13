class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        x = len(nums)
        y = len(newSet)

        if ( x == y):
            return  False
        elif (y < x):
            return True

        