T = int(input())
for i in range(T):
    N, X, S = [int(x) for x in input('').split()]
    list = []
    for j in range(S):
        A, B = [int(x) for x in input('').split()]
        if A != B:
            list.append([A,B])

    for k in list:
        if k[0] == X:
            X = k[1]
            
        elif k[1] == X:
             X = k[0]
             
    
    print(X)

