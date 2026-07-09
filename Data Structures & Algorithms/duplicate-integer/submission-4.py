class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid = False
        seen = set()
        for num in nums :
            if num in seen:
                valid = True
                return valid
            seen.add(num)
        return False
            

        