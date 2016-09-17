#https://www.hackerrank.com/contests/world-codesprint-6/challenges/abbr
q = int(input())
for i in range(q):
    a = list(input())
    b = list(input())
    flag = True
    for j in range(len(b)):
        elem = b[j]
        if ((elem not in a) and (chr(ord(elem)+32) not in a)) or (b[j].islower()):
            flag = False
            break
        elif (chr(ord(elem)+32) in a) and (elem not in a):
            a[a.index(chr(ord(elem)+32))] = chr(ord(a[a.index(chr(ord(elem)+32))])-32)
    len_a = len(a)
    k = 0
    while k<len_a:
        if a[k].islower():
            del(a[k])
            len_a -= 1
            k -= 1
        k+=1
    #print(a)
    if flag:
        if(a==b):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")