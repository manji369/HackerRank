#https://www.hackerrank.com/contests/w23/challenges/gravity-1
import math
def compute_levels(tree,start):
    depth_vertex = {}
    H = 0
    L = [start]
    depth_vertex[start] = 0
    while len(L) != 0:
        current_node = L.pop()
        for next in tree[current_node]:
            L.append(next)
            depth_vertex[next] = depth_vertex[current_node]+1
            H = max(H,depth_vertex[next])
    return depth_vertex,H
def fill_p1(T,L,tree,N):
    j_range = int(math.log(float(N),2))
    P = {}
    for i in xrange(N+1):
        P[i] = []
        for j in xrange(j_range):
            P[i].append(-1)
    for i in xrange(N+1):
        P[i][0] = T[i]
    for j in xrange(1,j_range):
        for i in xrange(N+1):
            if P[i][j-1] != -1:
                P[i][j] = P[P[i][j - 1]][j - 1]
    return P
def query(P,T,L,p,q):
    if L[p] < L[q]:
        tmp = p
        p = q
        q = tmp
    if L[p] != 0:
        log = int(math.log(float(L[p]),2))
    else:
        log = 0
    for i in xrange(log,-1,-1):
        if (L[p]-2**i)>=L[q]:
            p = P[p][i]
    if p == q:
        return p
    for i in xrange(log,-1,-1):
        if (P[p][i] != -1 and P[p][i] != P[q][i]):
            p,q = P[p][i],P[q][i]
    return T[p]
def inverse_search(v,u,tree,T):
    curr = u
    path = [u]
    while curr != v:
        curr = T[curr]
        path.append(curr)
    return path
def calc_gravity(lca,u,v,tree,dist_ref,D,T,H):
    if lca != v:
        dist = {}
        gravity = 0
        dist[v] = dist_ref + D[v]-D[lca]
        curr = v
        L = [v]
        gravity += dist[v]**2
        while len(L) > 0 and D[curr]<H:
            curr = L.pop(0)
            for next in tree[curr]:
                dist[next] = dist[T[next]]+1
                L.append(next)
                gravity += dist[next]**2
    else:
        gravity = 0
        path = inverse_search(v,u,tree,T)
        dist = {}
        dist[lca] = dist_ref
        curr = v
        L = [v]
        gravity += dist[lca]**2
        while len(L) > 0 and D[curr]<H:
            curr = L.pop(0)
            for next in tree[curr]:
                L.append(next)
                if next not in path:
                    dist[next] = dist[T[next]]+1
                else:
                    dist[next] = dist[T[next]]-1
                gravity += dist[next]**2
    return gravity
n = int(raw_input())
parents = map(int,raw_input().strip().split())
tree = {}
for i in xrange(1,n+1):
    tree[i] = []
for i in xrange(n-1):
    tree[parents[i]].append(i+2)
start = 1
q = int(raw_input())
T = {}
T[1] = 0
T[0] = 0
for i in xrange(2,n+1):
    T[i] = parents[i-2]
L,H = compute_levels(tree,1)
nr = int(math.sqrt(H))
P = fill_p1(T,L,tree,n)
for _ in xrange(q):
    u,v = map(int,raw_input().strip().split())
    depth_u = L[u]
    depth_v = L[v]
    lca = query(P,T,L,u,v)
    dist_anc_u = L[u] - L[lca]
    gravity = calc_gravity(lca,u,v,tree,dist_anc_u,L,T,H)
    print gravity