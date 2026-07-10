class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =  size = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[i])
            size = max(size, i - left + 1)
        return size
