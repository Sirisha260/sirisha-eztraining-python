'''inf = 9999999
N =5
G = [[0,19,5,0,0],[19,0,5,9,2],[5,5,0,1,6],[0,9,1,0,1],[0,2,6,1,0]]
selected_node = [0,0,0,0,0]
no_edge = 0
selected_node[0] = True
#printing for edge and weight
print("Edge: Weight\n")
while(no_edge<N-1):
    minimum = inf
    a=0
    b=0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if((not selected_node[n]) and G[m][n]):
                    #not in selected and there is an edge
                    if minimum> G[m][n]:
                        minimum = G[m][n]
                        a=m
                        b=n
                        print(str(a) +"-"+str(b)+":"+str(G[a][b]))
                        selected_node[b] = True
                        no_edge +=1
'''
#bellman ford algorithm:
from sys import maxsize
def BellmanFord(graph,V,E,src):
    dis = [maxsize] * V
    dis[src] = 0
    for i in range(V-1):
        for i in range(E):
            if dis[graph[j][0]]+graph[j][2]<dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]+graph[j][2]
    for i in range(E):
         x = graph[i][0]
         y = graph[i][1]
         weight =graph[i][2]
         if dis[x] != maxsize and dis[x] +weight<dis[y]:
            print("Graph contains negative weight cycle")
    print("Vertex Distance from Source")
    for i in range(V):
           print("%d\t\t%d" )                            











                        
                        
                        
