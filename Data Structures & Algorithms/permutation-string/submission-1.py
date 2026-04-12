import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Find substring in s2 having the following chars
        
        if len(s1) == 1:
            if s1 in set(s2):
                return True
            else:
                return False

        n = len(s1)
        
        # !!! Set is not correct, because sets won't contain duplicates.
        # just need to replace it with the right data structure gimme a sec
        chars = dict.fromkeys(string.ascii_lowercase, 0)
        currSet = dict.fromkeys(string.ascii_lowercase, 0)
        
        
        for i in range(n):
            chars[s1[i]] += 1

        for i in range(n):
            currSet[s2[i]] += 1

        
        ptr1 = 0
        ptr2 = n
        for i in range(len(s2)-n+1):
            
            print(currSet)

            if(currSet == chars):
                return True

            if(ptr2 >= len(s2)):
                return False

            currSet[s2[ptr1]] -= 1
            currSet[s2[ptr2]] += 1
            ptr2+=1
            ptr1+=1
        return False

        print(chars)
        print(currSet)
        





