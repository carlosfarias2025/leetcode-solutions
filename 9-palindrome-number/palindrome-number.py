class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        yStr = ""

        for i in reversed(xStr):
            yStr += i

        print(xStr)
        print(yStr)
        return yStr == xStr


solution = Solution()
print(solution.isPalindrome(101))