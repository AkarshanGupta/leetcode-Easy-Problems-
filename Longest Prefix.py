class Solution:
    def longestCommonPrefix(self, strs): #this line have the self because it will start from the start means 0th position 
        if len(strs) == 0:
            return ""

        prefix = strs[0]  # from here we are starting from the start of list 

        for i in range(len(prefix)): # this will iterate the first word character by charcater and compare it in the below loop 
            for word in strs[1:]:  # here we select the second word and and then we iterate character by character 
                if i == len(word) or word[i] != prefix[i]: # if the third word is less or small then we terminate from the algorithm
                    return prefix[:i] # this slice will return the prefix and stop where the i pointer is stopped

        return prefix
