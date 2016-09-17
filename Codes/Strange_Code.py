#https://www.hackerrank.com/challenges/strange-code
import sys
t = int(raw_input())
lb = 1
ub = 3
count = 1
while t>ub or t<lb:
    count *= 2
    lb = ub+1
    ub += (count*3)
    #print "lb "+str(lb)+" ub "+str(ub)
print ub-lb+1-(t-lb)