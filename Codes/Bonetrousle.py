#https://www.hackerrank.com/contests/world-codesprint-6/challenges/bonetrousle
import math
q = int(input().strip())
for i in range(q):
    n,k,b = list(map(int,input().strip().split()))
    p = n//b
    if b%2 == 0:
        l = list(range(p-(int(b/2)),p+int((b/2))))
        if l[0]<=0:
            add_val = 1-l[0]
            for temp in range(len(l)):
                l[temp] += add_val
    else:
        l = list(range(p-(b//2),p+(b//2)+1))
        if l[0]<=0:
            add_val = 1-l[0]
            for temp in range(len(l)):
                l[temp] += add_val
    s = n - sum(l)
    if s == 0:
        print(" ".join(map(str,l))) if l[-1] <= k else print(-1)
    elif s>0:
        range_diff = l[-1]-l[0]
        while s > range_diff:
            l.append(l[0]+range_diff+1)
            del(l[0])
            s -= (range_diff+1)
        if s == 0:
            print(" ".join(map(str,l))) if l[-1] <= k else print(-1)
        else:
            l.append(l[-1]+1)
            l.remove(l[-1]-s)
            print(" ".join(map(str,l))) if l[-1]<=k else print(-1)
    else:
        print(-1)