# Graph Algorithms
## Breadth-First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm that visits vertices level by level. Starting from a source vertex, BFS first visits all adjacent vertices and then moves to vertices at the next level. The algorithm uses a Queue data structure to maintain the order of traversal.

BFS guarantees the shortest path in an unweighted graph because vertices are explored in increasing order of distance from the source vertex. It systematically explores all neighboring vertices before proceeding deeper into the graph.

Advantages:

- Simple and systematic traversal.
- Finds shortest paths in unweighted graphs.
- Useful for connectivity analysis.

Disadvantages:

- Requires additional memory for queue storage.
- May consume large memory for dense graphs.

Applications:

- Shortest path in unweighted graphs.
- Social network analysis.
- Network broadcasting.
- Web crawling.
- Finding connected components.

Time Complexity:

```text
Adjacency List     O(V + E)
Adjacency Matrix   O(V²)
```

Space Complexity:

```text
O(V)
```

Important Examination Points:

- BFS uses Queue.
- Traverses graph level by level.
- Finds shortest path in unweighted graphs.
- Produces Breadth-First Tree.
- Frequently asked in NET, KSET, SET, and GATE examinations.

---

## Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal technique that explores a path completely before backtracking and exploring other paths. It uses a Stack data structure, either explicitly or through recursion.

DFS starts from a source vertex and repeatedly visits an unvisited adjacent vertex until no further progress is possible. It then backtracks to explore remaining branches.

Advantages:

- Requires less memory in many cases.
- Simple recursive implementation.
- Useful for exploring graph structure.

Disadvantages:

- Does not guarantee shortest path.
- May explore unnecessary paths.

Applications:

- Cycle detection.
- Topological sorting.
- Maze solving.
- Strongly connected components.
- Connectivity testing.

Time Complexity:

```text
Adjacency List     O(V + E)
Adjacency Matrix   O(V²)
```

Space Complexity:

```text
O(V)
```

Important Examination Points:

- DFS uses Stack or Recursion.
- Traverses graph depth-wise.
- Used in Topological Sorting.
- Used in Cycle Detection.
- Frequently asked in competitive examinations.

---

## Shortest Paths

The Shortest Path problem involves finding a path between two vertices such that the total distance or cost is minimum. It is one of the most important optimization problems in graph theory.

Shortest path algorithms are classified into Single Source Shortest Path and All-Pairs Shortest Path algorithms.

Dijkstra's Algorithm computes shortest paths from a source vertex when all edge weights are non-negative. Bellman-Ford Algorithm handles graphs with negative edge weights. Floyd-Warshall Algorithm computes shortest paths between all pairs of vertices.

Advantages:

- Minimizes travel cost and distance.
- Essential in routing applications.
- Improves network efficiency.

Applications:

- GPS navigation.
- Transportation systems.
- Network routing.
- Internet packet forwarding.
- Communication networks.

Time Complexity:

```text
Dijkstra         O((V + E) log V)
Bellman-Ford     O(VE)
Floyd-Warshall   O(V³)
```

Important Examination Points:

- Dijkstra does not support negative weights.
- Bellman-Ford supports negative weights.
- Floyd-Warshall gives all-pairs shortest paths.
- Frequently asked graph topic in competitive exams.

---

## Maximum Flow

The Maximum Flow problem determines the largest amount of flow that can be sent from a source vertex to a sink vertex in a flow network without violating edge capacity constraints.

A flow network consists of vertices connected by edges having capacities. The objective is to maximize the total flow reaching the sink.

The most popular algorithms are Ford-Fulkerson Algorithm and Edmonds-Karp Algorithm.

Advantages:

- Provides optimal utilization of networks.
- Useful in resource allocation problems.

Applications:

- Transportation networks.
- Communication systems.
- Supply chain management.
- Network routing.
- Project scheduling.

Time Complexity:

```text
Ford-Fulkerson    O(E × MaxFlow)
Edmonds-Karp      O(VE²)
```

Important Examination Points:

- Source sends flow.
- Sink receives flow.
- Residual Graph is used.
- Max-Flow Min-Cut Theorem is important.
- Ford-Fulkerson is the basic Maximum Flow algorithm.

---

## Minimum Spanning Trees (MST)

A Minimum Spanning Tree is a spanning tree of a connected weighted graph whose total edge weight is minimum among all possible spanning trees.

A spanning tree connects all vertices without forming any cycle and contains exactly V−1 edges, where V is the number of vertices.

The two most important algorithms for finding MST are Prim's Algorithm and Kruskal's Algorithm. Both are Greedy Algorithms.

Advantages:

- Produces minimum-cost network.
- Reduces infrastructure cost.
- Ensures complete connectivity.

Applications:

- Computer networks.
- Electrical networks.
- Road construction.
- Pipeline systems.
- Telecommunication networks.

Time Complexity:

```text
Prim's Algorithm      O(E log V)
Kruskal's Algorithm   O(E log E)
```

Important Examination Points:

- MST contains V−1 edges.
- No cycles are allowed.
- Prim's grows vertex-wise.
- Kruskal's grows edge-wise.
- Both are Greedy Algorithms.
- Very important topic for KSET, NET, SET, and GATE.