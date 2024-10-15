def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    def binSearch(arr):

        l,r = 0, len(arr) - 1


        while l <= r:
            mid = l + (r - l)//2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    

    for arr in matrix:  
        if binSearch(arr):
            return True

    
    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

res = searchMatrix(matrix, target)
print(res)