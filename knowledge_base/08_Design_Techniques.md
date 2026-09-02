# Design Techniques
## Divide and Conquer

Divide and Conquer is an algorithm design technique in which a problem is divided into smaller subproblems, each subproblem is solved independently, and the solutions are combined to obtain the final solution. It is one of the most powerful paradigms in computer science and forms the basis of many efficient algorithms.

The Divide and Conquer strategy consists of three major steps:

1. Divide the problem into smaller subproblems.
2. Solve the subproblems recursively.
3. Combine the solutions of the subproblems.

The efficiency of Divide and Conquer arises because large problems are reduced into smaller instances of the same problem. Many recursive algorithms follow this technique.

Famous algorithms based on Divide and Conquer include Merge Sort, Quick Sort, Binary Search, Strassen Matrix Multiplication, and Closest Pair of Points.

Advantages:

- Reduces problem complexity.
- Suitable for recursive implementation.
- Often provides better time complexity.
- Efficient for large datasets.

Disadvantages:

- Recursion overhead.
- Additional memory may be required.
- Combining subproblem solutions may be costly.

Complexities:

```text
Binary Search      O(log n)
Merge Sort         O(n log n)
Quick Sort Avg     O(n log n)
Quick Sort Worst   O(n²)
```

Important Examination Points:

- Based on Divide, Solve, and Combine phases.
- Merge Sort and Quick Sort use Divide and Conquer.
- Binary Search is a classical Divide and Conquer algorithm.
- Frequently solved using recurrence relations and Master Theorem.

---

## Dynamic Programming

Dynamic Programming is an algorithm design technique used to solve problems by breaking them into smaller overlapping subproblems and storing the results of previously solved subproblems to avoid repeated computation.

The central idea of Dynamic Programming is to solve each subproblem only once and reuse the stored result whenever required.

Dynamic Programming is applicable when:

- Problems exhibit Optimal Substructure.
- Problems contain Overlapping Subproblems.

Two major approaches are used:

1. Top-Down Approach (Memoization)
2. Bottom-Up Approach (Tabulation)

Dynamic Programming significantly improves efficiency compared to naïve recursive solutions because redundant computations are eliminated.

Applications include:

- Fibonacci Series
- Matrix Chain Multiplication
- Longest Common Subsequence
- Knapsack Problem
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm

Advantages:

- Eliminates repeated calculations.
- Improves time efficiency.
- Produces optimal solutions.

Disadvantages:

- Additional memory requirement.
- Difficult formulation for some problems.

Complexities:

```text
Fibonacci using DP                 O(n)
Matrix Chain Multiplication        O(n³)
0/1 Knapsack                      O(nW)
Longest Common Subsequence         O(mn)
```

Important Examination Points:

- Based on storing intermediate results.
- Uses Memoization and Tabulation.
- Requires Optimal Substructure.
- Requires Overlapping Subproblems.
- Frequently asked comparison with Divide and Conquer.

---

## Greedy Algorithms

A Greedy Algorithm is an algorithmic strategy that constructs a solution step-by-step by always choosing the locally optimal solution at each stage with the hope of obtaining a globally optimal solution.

A greedy algorithm never revisits earlier decisions. Once a choice is made, it cannot be changed.

Greedy methods are applicable when:

- Greedy Choice Property exists.
- Optimal Substructure Property exists.

Greedy algorithms are generally simple, fast, and easy to implement.

Applications include:

- Huffman Coding
- Prim's Algorithm
- Kruskal's Algorithm
- Dijkstra's Algorithm
- Job Sequencing Problem
- Activity Selection Problem

Advantages:

- Easy implementation.
- Fast execution.
- Low memory requirement.

Disadvantages:

- Does not always produce optimal solutions.
- Problem-specific applicability.

Complexities:

```text
Prim's Algorithm        O(E log V)
Kruskal's Algorithm     O(E log E)
Dijkstra's Algorithm    O(E log V)
Huffman Coding          O(n log n)
```

Important Examination Points:

- Makes locally optimal choices.
- Does not reconsider decisions.
- Prim's and Kruskal's Algorithms are Greedy Algorithms.
- Huffman Coding is a Greedy Algorithm.
- Frequently compared with Dynamic Programming.

---

## Backtracking

Backtracking is an algorithmic technique used to solve problems incrementally by building solutions step-by-step and abandoning a solution as soon as it is determined that it cannot lead to a valid final solution.

Backtracking systematically searches for a solution by exploring all possible alternatives and backtracking whenever a constraint is violated.

The process consists of:

1. Choose a candidate.
2. Check whether it is feasible.
3. Continue recursively.
4. Backtrack if the solution becomes invalid.

Backtracking is particularly useful for constraint satisfaction problems.

Applications include:

- N-Queens Problem
- Graph Coloring
- Hamiltonian Cycle
- Sudoku Solver
- Knight's Tour
- Subset Sum Problem

Advantages:

- Guarantees finding a solution if one exists.
- Reduces unnecessary exploration.
- Useful for combinatorial problems.

Disadvantages:

- May require exponential time.
- Not suitable for very large search spaces.

Complexities:

```text
N-Queens           O(N!)
Graph Coloring     Exponential
Hamiltonian Cycle  O(N!)
Subset Sum         O(2ⁿ)
```

Important Examination Points:

- Uses Depth First Search strategy.
- Rejects invalid partial solutions.
- N-Queens is the most frequently asked Backtracking problem.
- Graph Coloring and Hamiltonian Cycle are standard examples.

---

## Branch and Bound

Branch and Bound is an optimization technique used for solving combinatorial optimization problems. It systematically explores solution spaces by dividing them into branches and eliminates branches that cannot produce a better solution than the current best solution.

Unlike Backtracking, which focuses on feasibility, Branch and Bound focuses on finding the optimal solution.

The method consists of:

1. Branching: Divide the problem into subproblems.
2. Bounding: Compute upper or lower bounds.
3. Pruning: Discard non-promising solutions.

Branch and Bound reduces computation by avoiding exploration of unnecessary branches.

Applications include:

- Travelling Salesman Problem (TSP)
- 0/1 Knapsack Problem
- Assignment Problem
- Job Scheduling
- Integer Programming

Advantages:

- Produces optimal solutions.
- Reduces search space.
- More efficient than exhaustive search.

Disadvantages:

- High memory requirement.
- Complexity may still be exponential.

Complexities:

```text
TSP                    O(2ⁿ) to O(n!)
0/1 Knapsack           Exponential
Assignment Problem     Exponential
```

Important Examination Points:

- Used for optimization problems.
- Branch = Divide solution space.
- Bound = Compute best possible value.
- Pruning removes non-promising nodes.
- Differs from Backtracking because it seeks optimal solutions rather than just feasible solutions.
- Frequently asked comparison: Backtracking vs Branch and Bound.