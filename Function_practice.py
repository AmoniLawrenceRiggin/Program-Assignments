def fibanocciFinder (max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k
    return("Fibonacci yay!")

def primeFinder (max):
    for i in range(2,max):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
    return(max)

    #print(fibonacciFinder(100), primeFinder(15))


n = 5
m = 5
areaList = [0]*n*m
for b in range(0,n):
    for h in range(0,m):
        areaList[i] = triangleArea(b,h)
        i += 1
print(areaList)