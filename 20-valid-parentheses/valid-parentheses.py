output1 = ['(','[','{']
output2 = [')',']','}']

class Solution:
    def isValid(self, s: str) -> bool:
        charcurrent = ''
        indexElement1 = -1
        chars = []

        for i in range(len(s)):
            if s[i] in output1:
                chars.append(s[i])
                charcurrent = s[i]
                indexElement1  = output1.index(s[i])
            else:
                if not chars:
                    return False
                if output2.index(s[i]) == indexElement1:
                    charLastList = chars[len(chars)-2]
                    chars.pop()
                    indexElement1 = output1.index(charLastList)
                else:
                    return False
                    

        if len(chars) > 0 or indexElement1 == -1:
            return False
        else:
            return True 
      
                    
            

example1 = "()"
example2 = "()[]{}"
example3 = "(]"
example4 = "([])"
example5 = "([)]"

solution = Solution()
print(solution.isValid(example1)) #Expected True
print(solution.isValid(example2)) #Expected True
print(solution.isValid(example3)) #Expected False
print(solution.isValid(example4)) #Expected True
print(solution.isValid(example5)) #Expected False