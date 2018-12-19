'''
HackerLand University has the following grading policy:
Every student receives a in the inclusive range from to .
Any less than is a failing grade.
Sam is a professor at the university and likes to round each student's according to these rules:
If the difference between the and the next multiple of is less than , round up to the next multiple of .
If the value of is less than , no rounding occurs as the result will still be a failing grade.
For example, will be rounded to but will not be rounded because the rounding would result in a
number that is less than .
'''
n = int(input())
new = []
for i in range(n):
    k = int(input())
    q = k%5
    l = int((k /5))+1
    if q == 0:
        new.append(k)
    else:
        p = (l*5) - k
        if k<38:
            new.append(k)
        elif p < 3:
            a = l*5
            new.append(a)
        elif p == 3:
            new.append(k)
        else:
            new.append(k)

          
for i in range(n):
    print(new[i])
    
