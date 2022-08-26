import math

def Sieve(m,n):
    temp = [True for k in range(n+1)]
    max_div = math.floor(math.sqrt(n))

    for i in range(2,n+1):
        if temp[i] == True:
            for j in range(2*i,n+1,i):
                temp[j] = False

    temp[1] = False
    temp[0] = False

    primes = []

    for i in range(len(temp)):
        if temp[i] == True and i>=m:
            primes.append(i)

    return primes

t = int(input(''))
mn = []

for i in range (t):
    m,n = map(int, input().split())
    mn.append(m)
    mn.append(n)

from datetime import datetime
start_time = datetime.now()

for i in range(0,len(mn)-1,2):
    tab = Sieve(mn[i],mn[i+1])
    for i in tab:
        print(i)
    print('')

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
Footer
© 2022 GitHub, Inc.