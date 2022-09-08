arr = [1,4,8,6,9,3,4,5,20,19]
high = 0
result = 0

for i in arr :
    if i > high : 
        result = high
        high = i
    else :
        if i > result :
            result = i 

print(result)
    