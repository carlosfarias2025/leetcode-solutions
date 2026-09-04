class Solution:
    def reverse(self, x: int) -> int:
        intStr = str(x)
        negative = False
        numreturn = 0
        
        if "-" in intStr:
            negative = True
            intStr = intStr[1:]
            
        for i in range(len(intStr),0,-1):
            numreturn += (int(intStr[i-1])*(10**(i-1)))
            
        
        if numreturn > 2147483647:
            numreturn = 0
        if negative:
            numreturn = -numreturn
        return numreturn

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
