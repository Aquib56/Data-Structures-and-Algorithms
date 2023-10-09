class Solution(object):
    def checkStrings(self, s1, s2):
        if len(s1) != len(s2):
            return False

        even_freq_s1 = [0] * 26
        odd_freq_s1 = [0] * 26

        even_freq_s2 = [0] * 26
        odd_freq_s2 = [0] * 26

        for i in range(len(s1)):
            if i % 2 == 0:
                even_freq_s1[ord(s1[i]) - ord('a')] += 1
                even_freq_s2[ord(s2[i]) - ord('a')] += 1
            else:
                odd_freq_s1[ord(s1[i]) - ord('a')] += 1
                odd_freq_s2[ord(s2[i]) - ord('a')] += 1
        return even_freq_s1 == even_freq_s2 and odd_freq_s1 == odd_freq_s2
s1="abcdba"
s2="cabdab"
s=Solution()
print(s.checkStrings(s1,s2))