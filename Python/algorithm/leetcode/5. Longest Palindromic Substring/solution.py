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
