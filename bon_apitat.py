'''
Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is
allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must
determine if his calculation is correct.
'''
t = int(input())
for i in range(t):
    sum =  0
    p, j = [int(x) for x in input().split()]
    arr = []
    arr = [int(i) for i in input().split()]
    c = int(input())
    for k in range(p):
        if k != j:
            sum = sum + arr[k]

    bact = sum /2
    dif = int(c - bact)

    if bact == c:
        print("Bon Appetit")
    else:
        print(dif)
    
