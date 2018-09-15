#code of codeagon on hacker rank
n = int(input())
arr = []
arr = [int(i) for i in input().split()]
#taking empty list
foo = []
sum = 0
for i in range(0, n):
    for j in range(i, n):
        if i==j:
            ans = arr[i]|arr[j]
            foo.append(ans)
            sum = sum + foo[len(foo)-1]
        else:
            ans = foo[len(foo)-1]|arr[j]
            foo.append(ans)
            sum = sum + foo[len(foo)-1]

print(sum)
        


