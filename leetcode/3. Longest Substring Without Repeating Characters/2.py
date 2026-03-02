class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        left = 0
        max_lenght = 0
        for i, num in enumerate(s):
            if num in hash:
                if hash[num] >= left:
                    left = hash[num] + 1
                
            lenght = i - left + 1
            if lenght > max_lenght:
                max_lenght = lenght
            
            hash[num] = i
        return max_lenght