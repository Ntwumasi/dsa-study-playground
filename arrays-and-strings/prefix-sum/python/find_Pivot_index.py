# 724. Find Pivot Index

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