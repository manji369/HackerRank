#https://www.hackerrank.com/contests/w23/challenges/lighthouse
def find_max_rad(L,x,y,n):
    r = 0
    flag = False
    while r <=50:
        for i in xrange(-(r+1),r+2):
            if flag:
                break
            for j in xrange(-(r+1),r+2):
                if (i**2+j**2 <= (r+1)**2):
                    if x+i>=n or x+i<0 or y+j>=n or y+j<0:
                        flag = True
                        break
                    elif L[x+i][y+j] != '.':
                        flag = True
                        break
        if not flag:
            r += 1
        else:
            break
    return r
n = int(raw_input().strip())
L = []
for _ in xrange(n):
    L.append(raw_input().strip())
r_max = 0
count = 0
for i in xrange(n):
    for j in xrange(n):
        if L[i][j] == '.':
            r_max = max(r_max,find_max_rad(L,i,j,n))
print r_max