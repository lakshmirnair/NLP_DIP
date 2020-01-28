def edit_distance(s1,s2):
    m = len (s1) +1
    n = len (s2) +1
    dist = {}
    for i in range(m):
        dist [i,0] = i
    for j in range(n):
        dist [0,j] = j
    for i in range(1, m):
        for j in range(1, n):
            if (s1[i-1] == s2[j-1]):
                c = 0
            else:
                c = 2
            dist[i,j] = min(dist[i,j-1]+1, dist[i-1, j]+1, dist[i-1,j-1]+c)
    return dist[i,j]
print(edit_distance("medium","enum"))
print(edit_distance("peace","piece"))
