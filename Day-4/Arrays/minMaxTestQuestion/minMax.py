# Question : 


arr = [4, 2, 1, 6, 10, 12, 3, 17, 9]

i = 1
minMax = False
result = []

while i < len(arr)-1:
    if arr[i+1] < arr[i] and arr[i-1] < arr[i] or arr[i+1] > arr[i] and arr[i-1] > arr[i] :
        minMax = True
        
    if arr[i+1] > arr[i-1] and not minMax:
        arr.pop(i)
        i-=1
    elif arr[i+1] < arr[i-1] and not minMax :
        arr.pop(i)
        i-=1
    
    i+=1 
    minMax = False

print(arr)
    
# Intution : find the local min and max of the array 