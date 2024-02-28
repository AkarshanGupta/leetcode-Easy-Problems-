# the basic idea is we have to create dictionary for the alphabets whichh are related to the numbers
# we have a look on the example the combination are a->b not b->a

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if digits == "":
            return []

        numbers = list(phone_map[digits[0]]) # so here we will select the start number and then start the combiation by iterating it 

        for digit in digits[1:]: # now here we will start the slicing for the rest of numbers
            numbers = [old + new for old in numbers for new in list(phone_map[digit])] # now to get all the combination together we use nested for loops
                                                      # this loops nested loops decrease the time complexity
        return numbers 