class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
        for item in items:
            if item[index] == ruleValue:
                res += 1
        return res
        




        