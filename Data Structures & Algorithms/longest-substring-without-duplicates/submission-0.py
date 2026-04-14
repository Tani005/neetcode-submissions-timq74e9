class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
                return 0
        
        seen = set()
        i = 0 
        j = 0
        max_len = 0

        while j < len(s):            
            if s[j] not in seen:
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1

            else:
                seen.remove(s[i])
                i += 1

        return max_len
        

        