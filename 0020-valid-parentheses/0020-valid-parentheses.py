class Solution:
    def isValid(self, s: str) -> bool:
        strs = list(s)
        pair = {'(':')','{':'}','[':']'}
        key = pair.keys()
        stack = []
        for i in range(len(strs)):
            if strs[i] in key: 
                stack.append(strs[i])
            else:
                if not stack:
                    return False
                a = stack.pop()
                if pair[a] != strs[i]:
                    return False
        
        if not stack:
            return True
        else:        
            return False
