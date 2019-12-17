dim = 10
arr = [[" " for i in range(dim)] for j in range(dim)]

def printArr(arr):
    for array in reversed(arr):
        print(array[::-1])

printArr(arr)