class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mg = list(magazine)
        if not mg and ransomNote:
            return False
        if not mg and not ransomNote:
            return True
        for i in ransomNote:
            if i not in mg:
                return False
            else:
                mg.remove(i)
        return True