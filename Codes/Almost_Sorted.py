#https://www.hackerrank.com/challenges/almost-sorted
n = int(raw_input())
arr = list(map(int,raw_input().split()))
arr1 = arr[:]
arr1.sort()
count = 0
l = []
l1 = []
not_swapped = True
no_swaps = False
for i in xrange(len(arr)):
    if arr[i] != arr1[i]:
        count += 1
        l.append(i)
#print(arr)
if count == 2:
    print "yes"
    print "swap "+str(l[0]+1)+" "+str(l[1]+1)
    not_swapped = False
if count == 0:
    print "yes"
    no_swaps = True
if not_swapped and not no_swaps:
    #print "entered"
    printed_no = False
    start = -1
    end = -1
    rev_i = 0
    rev_j = 0
    count = False
    for i in xrange(len(arr)-1):
        if arr[i+1] < arr[i] and not count:
            if start > -1:
                end += 1
                #print "end " + str(end)
            else:
                start = i
                #print "start " + str(start)
                end = i
        else:
            if start != -1:
                count = True
                rev_i = start+1
                start = -1
                rev_j = end+1
                end = -1
        if arr[i+1] < arr[i] and count:
            print "no"
            printed_no = True
            break
    if rev_j != 0 and rev_i != rev_j and not printed_no:
        print "yes"
        print "reverse "+str(rev_i)+" "+str(rev_j+1)
    else:
        if not printed_no:
            print "no"
    #print rev_i
    #print rev_j