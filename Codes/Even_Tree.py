#https://www.hackerrank.com/challenges/even-tree
def find_num(dict,child):
    children = dict[child][:]
    num = len(children)
    while children:
        next_child = children.pop()
        num += find_num(dict,next_child)
    return num
N,M = map(int,raw_input().strip().split())
dict = {}
for i in xrange(1,N+1):
    dict[i] = []
for i in xrange(M):
    e2,e1 = map(int,raw_input().strip().split())
    dict[e1].append(e2)
#print dict
count = 0
current  = 1
S = dict[current][:]
current_path = [1]
while current_path:
    current = current_path[0]
    S = dict[current][:]
    current_path.extend(S)
    #print "cr_path " + str(current_path) + " cr " + str(current) + " S " + str(S) + " count " + str(count) + " d " + str(dict)
    while S:
        child = S.pop()
        num = 1+find_num(dict,child)
        if num%2==0:
            dict[current_path[0]].remove(child)
            count += 1
    current_path.pop(0)
print count