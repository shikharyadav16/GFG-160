# Strings rotations of Each other

class Solution:
    def areRotations(self, s1, s2):
        
        def findLps(pat):
            n = len(pat)
            lps = [0]*n
            
            i = 1
            len_lps = 0
            
            while (i < n):
                
                if (pat[i] == pat[len_lps]):
                    len_lps += 1
                    lps[i] = len_lps
                    i += 1
                    
                else:
                    
                    if (len_lps != 0):
                        len_lps = lps[len_lps - 1]
                        
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        s = s1 + s1
        lps = findLps(s2)
        
        i = j = 0
        while (i < len(s)):
            
            if (s[i] == s2[j]):
                i += 1
                j += 1
                
                if (j == len(s2)):
                    return True
                    
            elif (s2[j] != s[i] and i < len(s)):
                
                if (j != 0):
                    j = lps[j - 1]
                
                else:
                    i += 1
            
        return Falses = s1 + s1
        if (s2 in s):
            return True
        return False
            
            
        
                    
