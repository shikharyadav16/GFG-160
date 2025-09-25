#   Minimum Characters to add for palindrome

class Solution:   
    def minChar(self, s):
        def findLps(pat):
            n = len(pat)
            lps = [0]*n

            len_lps = 0
            i = 1

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

            return lps[-1]

        revS = s[::-1]
        num = findLps(s + "$" + revS)

        return len(s) - num
        
        
