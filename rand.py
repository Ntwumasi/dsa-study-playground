# type("Hello, World")
# concatenation
var1 = "abra"
var2 = "cadabra"
magic_string = var1 + var2
# indexing
print(magic_string[0])
print(magic_string[-1])



'''
prefix sum work and study

'''

def fn(arr):
    prefix = [arr[0]]
    # added the first value from the array into the prefix
    for i in range(1, len(arr)):
    # loop through the array starting from the second element    
        prefix.append(prefix[-1] + arr[i]
    return prefix



# find mid point 
# lets find the total we can use the built in operator sum()
# then for now lets declare the leftsumn to 0 
# then we loopthorugh and do the computation 
# if leftside eqauls rightside then we return the current iterrable
# else we return the last element of the array
# 

 class solution:
    def findMid(self, arr:int) -> int:
        totalSum = sum(arr)
        leftSum = 0
        for i in range(len(arr)):
            rightSum = totalSum - leftSum - arr[i]
            if leftSum == rightSum
                return i
            leftSumn += arr[i] 

         return -1  