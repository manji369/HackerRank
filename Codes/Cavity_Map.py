#https://www.hackerrank.com/challenges/cavity-map
import sys
n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)
for i in xrange(0,n):
    for j in xrange(0,n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            sys.stdout.write(grid[i][j])
        else:
            flag = False
            for i1 in [-1,1]:
                if i+i1>=0 and i+i1<=n-1:
                    if grid[i][j] <= grid[i+i1][j]:
                        flag = True
                        #print "i "+str(i)+" j "+str(j)+" i+i1 "+str(i+i1)+" j+j1 "+str(j+j1)
            for j1 in [-1,1]:
                if j+j1>=0 and j+j1<=n-1:
                    if grid[i][j] <= grid[i][j+j1]:
                        flag = True
                        #print "i "+str(i)+" j "+str(j)+" i+i1 "+str(i+i1)+" j+j1 "+str(j+j1)
            if flag:
                sys.stdout.write(grid[i][j])
            else:
                sys.stdout.write("X")
    print