# Sample Input 1:

# 1
# 3 5
# 1 2 2 3 1

# Sample Output 1:

# 4

# Explanation of sample input 1:

# The ayush will read the chapter as follows,
# Day 1 : 1 , 2         Time required : 3
# Day 2 : 3             Time required : 2
# Day 3 : 4 , 5         Time required : 4
# So the maximum time in a day is 4.

# Sample Input 2:

# 1
# 4 7
# 2 2 3 3 4 4 1 

# Sample Output 2:

# 6

# Explanation of sample input 2:

# The ayush will read the chapter as follows,
# Day 1 : 1 , 2          Time required : 4
# Day 2 : 3 , 4          Time required : 6
# Day 3 : 5              Time required : 4
# Day 4 : 6 , 7          Time required : 5
# So the maximum time in a day is 6.


# if Ayush want to study 6 chapters in 3 days and the time that each chapter requires is as follows:
# Chapter 1 = 30
# Chapter 2 = 20
# Chapter 3 = 10
# Chapter 4 = 40
# Chapter 5 = 5
# Chapter 6 = 45

# Then he will study the chapters in the following order 

# | day 1 : 1 , 2 | day 2 : 3 , 4 | day 3 : 5 , 6 |
# Here we can see that he study chapters in sequential order and the maximum time to study on a day is 50, which is the minimum possible in this case.

def ayushGivesNinjatest(n, m, time):
    # Write your code here.
    
    def safeToAllocate(mid):
        day = 1
        total = 0
        for i in time :
            if i > mid : return False 
            if total + i > mid :
                day+=1
                total = i 
            else :
                total += i
        if day <= n :
            return True
        else:
            return False
        
    low = 0
    high = 0
    result = float("inf")
    for i in time : 
        high += i
    
    while low <= high :
        mid = (low + high) // 2 
        
        if safeToAllocate(mid) :
            high = mid - 1
            result = mid
        
        else :
            low = mid + 1
         
    return result
        
        
    
