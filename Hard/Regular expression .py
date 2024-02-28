#here we have used dp(dynamic programming) and which makes this algorithm more faster
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}   # this is memoniazation which stores the previous value of the string which makes the algo faster because we are ot calculating it not again and agian

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p): # here we are running two pointer to keep track of track which strings which are being read
                return True # we will chcek the lenght of the both string if the first stirng is same or greater then the second string then it will be true 

            if j >= len(p):
                return False # this is vice versa because we are comparing with the first string

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')  # here we are checking for the what are the contents of second string and then returning it 
            if j + 1 < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2)) or (match and (dfs(i + 1, j)))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)
