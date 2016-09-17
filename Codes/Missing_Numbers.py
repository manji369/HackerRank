#https://www.hackerrank.com/challenges/missing-numbers
from collections import Counter
count1 = Counter()
count2 = Counter()
n = int(raw_input().strip())
L1 = map(int,raw_input().strip().split())
m = int(raw_input().strip())
L2 = map(int,raw_input().strip().split())
miss_count = 0
miss = []
for i in xrange(n):
    count1[L1[i]] += 1
    count2[L2[i]] += 1
for i in xrange(n,m):
    count2[L2[i]] += 1
for key,item in count2.iteritems():
    if count1[key]!=item:
        miss_count += item-count1[key]
        miss.append(key)
print " ".join(map(str,sorted(miss)))