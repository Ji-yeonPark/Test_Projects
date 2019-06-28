# solution 01 : 6396 ms / 13.2 MB / python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1 or s == s[::-1]:
            return s

        palindrome = ""
        for i in range(len(s)):
            j = i + 1
            while j <= len(s):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(palindrome):
                    palindrome = s[i:j]
                j += 1
        return palindrome

    

# solution 02 : 4384 ms / 13.1 MB / python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1 or s == s[::-1]:
            return s
        
        p = ""
        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)+1):
                str = s[i:j]
                if str == str[::-1] and len(p) < len(str):
                    p = str
        return p
