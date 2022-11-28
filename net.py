# Python3 program to find the shortest
# path between any two nodes using
# Floyd Warshall Algorithm.

# Initializing the distance and
# Next array
def initialise(V):
    global dis, Next

    for i in range(V):
        for j in range(V):
            dis[i][j] = graph[i][j]

            # No edge between node
            # i and j
            if (graph[i][j] == INF):
                Next[i][j] = -1
            else:
                Next[i][j] = j


# Function construct the shortest
# path between u and v
def constructPath(u, v):
    global graph, Next

    # If there's no path between
    # node u and v, simply return
    # an empty array
    if (Next[u][v] == -1):
        return {}

    # Storing the path in a vector
    path = [u]
    while (u != v):
        u = Next[u][v]
        path.append(u)

    return path


# Standard Floyd Warshall Algorithm
# with little modification Now if we find
# that dis[i][j] > dis[i][k] + dis[k][j]
# then we modify next[i][j] = next[i][k]
def floydWarshall(V):
    global dist, Next
    for k in range(V):
        for i in range(V):
            for j in range(V):

                # We cannot travel through
                # edge that doesn't exist
                if (dis[i][k] == INF or dis[k][j] == INF):
                    continue
                if (dis[i][j] > dis[i][k] + dis[k][j]):
                    dis[i][j] = dis[i][k] + dis[k][j]
                    Next[i][j] = Next[i][k]
    print(Next)


# Print the shortest path
def printPath(path):
    n = len(path)
    for i in range(n - 1):
        print(path[i], end=" -> ")
    print(path[n - 1])


# Driver code
if __name__ == '__main__':
    MAXM, INF = 100, 10 ** 7
    dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

    V = 4
    graph = [
        [0, 5, 999, 999],
        [15, 0, 15, 5],
        [30, 999, 0, 15],
        [15, 999, 5, 0]
    ]

    # Function to initialise the
    # distance and Next array
    initialise(V)

    # Calling Floyd Warshall Algorithm,
    # this will update the shortest
    # distance as well as Next array
    floydWarshall(V)
    path = []

    # # Path from node 1 to 3
    # print("Shortest path from 1 to 3: ", end="")
    # path = constructPath(1, 3)
    # printPath(path)

    # Path from node 0 to 2
    print("Shortest path from 0 to 2: ", end="")
    path = constructPath(0, 2)
    printPath(path)

    # Path from node 3 to 2
    # print("Shortest path from 3 to 2: ", end="")
    # path = constructPath(3, 2)
    # printPath(path)

# This code is contributed by mohit kumar 29
