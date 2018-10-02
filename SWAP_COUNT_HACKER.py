n = int(input())
arr = []
arr = [int(i) for i in input().split()]
t = 0
def bubbleSort(arr, t):
    t = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                t = t + 1
    print("Array is sorted in {} swaps.".format(t))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))

bubbleSort(arr, t)
 

