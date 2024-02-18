class Solution:
    def maxArea(self, height: List[int]) -> int:    
        max_area = 0   #here we are declaring the area of the conatiner so that we can store our result 
        l = 0 
        r = len(height)-1  # here we are declaring two variables and using to navigate just 
                           # just like quick sort 
        while l < r:  # here we iterate through the loop 
            area = (r-l)*min(height[r], height[l]) 
            max_area = max(max_area, area)
            if height[l] < height[r]: # incrementing the pointer 
                l += 1
            else:
                r -= 1
        return max_area

 