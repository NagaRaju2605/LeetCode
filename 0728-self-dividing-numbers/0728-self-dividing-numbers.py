class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []

        for n in range(left, right + 1):
            temp = n
            valid = True

            while temp > 0:
                digit = temp % 10

                if digit == 0 or n % digit != 0:
                    valid = False
                    break

                temp = temp // 10

            if valid:
                ans.append(n)

        return ans