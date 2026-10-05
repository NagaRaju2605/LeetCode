class Solution:
    def findAnagrams(self, s: str, p: str):
        ans = []
        n = len(p)

        p_count = [0] * 26
        s_count = [0] * 26

        for c in p:
            p_count[ord(c) - ord('a')] += 1

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            if i >= n:
                s_count[ord(s[i-n]) - ord('a')] -= 1

            if s_count == p_count:
                ans.append(i - n + 1)

        return ans