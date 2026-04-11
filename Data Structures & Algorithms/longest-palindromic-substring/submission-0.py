class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        max_length = 0
    
        for i in range(len(s)):
            # 奇數長度
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    result = s[left : right + 1]
                left = left - 1
                right = right + 1
            
            # 偶數長度
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    result = s[left : right + 1]
                left = left - 1
                right = right + 1
        
        return result






# coming fron two side together