import os
from random import choice
folders = os.listdir()

allFiles = []
path = os.getcwd()
for folder in folders:
    if "." not in folder:
        os.chdir(f"{path}\{folder}") 
        subFolders = os.listdir()
        allFiles.extend(subFolders)



for i in range(5):
    print(f"{i+1}. {choice(allFiles)}")






def maximumSubarray(nums):

    sum = nums[0]

    m = sum
    for i in range(1, len(nums)):
        if sum < 0: 
            sum = nums[i]
        else:
            sum += nums[i]
        m = max(m, sum)


    return m
arr = [1,2,3,-1,-3,2,4,-6,1]
res = maximumSubarray(arr)
print(res)


def printInSpiralManner(matrix):


    
    RL = len(matrix[0])
    CL = len(matrix)

    def printSpiral(matrix, rl, cl, r, c):

        if r == rl//2 and c == cl//2:
            return 

        while r == rl//2 and c == cl//2:


    01, 02, 03, 13, 23, 22, 21, 10, 11 


    pass