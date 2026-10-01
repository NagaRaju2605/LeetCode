class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        ans = ""
        for ch in sorted(d, key = lambda x:d[x], reverse = True):
            ans += ch * d[ch]
        return ans
        