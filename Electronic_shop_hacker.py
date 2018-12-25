b, n,m = [int(i) for i in input().split()]
arr= []
arr =[int(i) for i in input().split()]
arr2 = []
arr2 =[int(i) for i in input().split()]
arr3 = []
for i in range(n):
    s = 0
    for j in range(m):
        s = arr[i] + arr2[j]
        if s<=b:
            arr3.append(s)
        s = 0
arr3.sort(reverse = True)
if not arr3:
    print("-1")
else:
    print(arr3[0])
