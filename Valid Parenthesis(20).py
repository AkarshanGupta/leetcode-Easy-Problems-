class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # creating a stack using list 
        pairs = {   #creating dictionary so that we can check for the open and closed bracket with the key value pair
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:  # from here we start iterate through the list 
            if bracket in pairs: # here we check if it is open or close 
                stack.append(bracket) # if it is open we append it in the list 
            elif len(stack) == 0 or bracket != pairs[stack.pop()]: # if encounter close bracket then we pop the open bracket from the list 
                return False # if the above conditon fails we create return false because there are not matching string 

        return len(stack) == 0 