#https://www.hackerrank.com/contests/world-codesprint-6/challenges/flipping-the-matrix
T = int(input())
for _ in range(T):
    n = int(input())
    l = []
    for _l in range(2*n):
        l.append(list(map(int,input().split())))
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += max(l[i][j],l[2*n-i-1][j],l[i][2*n-j-1],l[2*n-i-1][2*n-j-1])
    print(sum)