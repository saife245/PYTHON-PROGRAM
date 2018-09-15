#xor quaries of codeagon on hackerrank
n = int(input())
list = []
for _ in range(n):
    x, l, r =[int(x) for x in input().split()]
    list.append([x, l, r])

#taking empty list
xor = []

for k in list:
    for i  in range((k[2]-k[1])+1):
        ans = k[0]^(k[1]+i)
        xor.append(ans)
        print(xor)
    xor.sort(reverse = True)
    print(xor[0])
    del xor[:]
