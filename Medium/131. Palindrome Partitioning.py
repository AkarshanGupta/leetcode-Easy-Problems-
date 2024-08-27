class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            return substring == substring[::-1]

        def dfs(start, path, result):
            if start == len(s):
                result.append(path[:])
                return 

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    dfs(end, path,result)
                    path.pop()

        result = []
        dfs(0,[],result)
        return result 
