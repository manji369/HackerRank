#https://www.hackerrank.com/challenges/new-year-chaos
import sys
T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    exchanges = True
    passnum = len(q)-1
    bribes = 0
    flag = True
    for i, v in enumerate(q):
        if (v-1)-i > 2:
            flag = False
            break
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if q[i]>q[i+1]:
                exchanges = True
                bribes += 1
                temp =  q[i]
                q[i] = q[i+1]
                q[i+1] = temp
        passnum = passnum-1
    print(bribes) if flag else print("Too chaotic")