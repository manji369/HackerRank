#https://www.hackerrank.com/challenges/bigger-is-greater
n = int(input())
def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
    return a
for _ in range(n):
    s = input()
    l = list(s)
    max_i = 0
    max_j = 0
    for i in range(1,len(l)):
        if l[i-1]<l[i]:
            max_i = i
    if max_i == 0:
        print("no answer")
        continue
    for j in range(max_i,len(l)):
        if l[j]>l[max_i-1]:
            max_j = j
    l = swap(l,max_j,max_i-1)
    a = l[max_i+0:]
    a.sort()
    for k in range(max_i,len(l)):
        l[k] = a[k-max_i]
    print("".join(l))