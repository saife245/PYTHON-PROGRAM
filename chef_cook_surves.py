#every k iteration serve changes
#first chef serve
#p1 and p2 is point of chef and cook
#predict whose turn after p1 and p2 point

t = int(input())
for i in range(t):
    p1, p2, k = [int(x) for x in input().split()]
    y = 0
    sum = 0
    sum = p1 + p2
    while sum >=k:
        sum= sum - k
        y = y + 1

    if y%2==0:
        print("CHEF")
    else:
        print("COOK")
