class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        ans = 0
        for i in s:
            d[i] = d.get(i , 0 ) + 1
        for n in d.values():
            ans += (n // 2) * 2
            if ans % 2 == 0 and n % 2 == 1:
                ans += 1
        return ans



        