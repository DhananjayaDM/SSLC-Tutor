# Complexity Theory
## P and NP Class Problems

The theory of computational complexity classifies problems according to the amount of computational resources required to solve them. Two of the most important complexity classes are **P** and **NP**.

**Class P (Polynomial Time)** consists of decision problems that can be solved by a deterministic algorithm in polynomial time. A problem belongs to class P if its running time can be expressed as a polynomial function of the input size, such as O(n), O(n²), O(n³), or O(n log n). Problems in P are considered computationally tractable because efficient algorithms exist for solving them.

Examples of P-class problems include:

- Binary Search
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Minimum Spanning Tree
- Shortest Path Problem (Dijkstra's Algorithm)
- Sorting Algorithms

**Class NP (Nondeterministic Polynomial Time)** consists of decision problems for which a proposed solution can be verified in polynomial time by a deterministic algorithm. In other words, even if finding the solution is difficult, checking whether a given solution is correct can be done efficiently.

A problem belongs to NP if:

- A solution can be guessed.
- The guessed solution can be verified in polynomial time.

Examples of NP problems include:

- Travelling Salesman Problem (Decision Version)
- Hamiltonian Cycle Problem
- Graph Coloring Problem
- Clique Problem
- Subset Sum Problem
- Knapsack Problem

Relationship between P and NP:

```text
P ⊆ NP
```

Every problem that can be solved in polynomial time can also be verified in polynomial time.

One of the most important unsolved questions in Computer Science is:

```text
Is P = NP ?
```

If P = NP, then every problem whose solution can be verified quickly can also be solved quickly. Despite decades of research, this question remains unanswered.

Applications:

- Algorithm Design
- Optimization Problems
- Artificial Intelligence
- Scheduling Systems
- Cryptography
- Computational Complexity Analysis

Important Examination Points:

- P = Problems solvable in polynomial time.
- NP = Problems verifiable in polynomial time.
- Every P problem belongs to NP.
- Relationship: P ⊆ NP.
- "P vs NP" is one of the seven Millennium Prize Problems.

---

## NP-Completeness and Reducibility

NP-Completeness is one of the most important concepts in Computational Complexity Theory. It helps classify difficult problems for which no efficient polynomial-time solution is known.

A problem is said to be **NP-Complete** if:

1. The problem belongs to NP.
2. Every problem in NP can be transformed into it in polynomial time.

An NP-Complete problem is therefore one of the hardest problems in NP. If a polynomial-time algorithm is found for any NP-Complete problem, then every problem in NP can also be solved in polynomial time.

Conditions for NP-Completeness:

```text
Problem ∈ NP
AND
NP-Hard
```

Therefore:

```text
NP-Complete = NP ∩ NP-Hard
```

Examples of NP-Complete Problems:

- Boolean Satisfiability Problem (SAT)
- 3-SAT Problem
- Clique Problem
- Vertex Cover Problem
- Hamiltonian Cycle Problem
- Travelling Salesman Problem (Decision Version)
- Subset Sum Problem
- Graph Coloring Problem

**NP-Hard Problems** are at least as difficult as NP problems. An NP-Hard problem may or may not belong to NP because its solution may not be verifiable in polynomial time.

Relationship among classes:

```text
P ⊆ NP ⊆ NP-Hard

NP-Complete = NP ∩ NP-Hard
```

Reducibility is a technique used to compare the difficulty of computational problems.

A problem A is reducible to problem B if any instance of problem A can be transformed into an instance of problem B in polynomial time.

Notation:

```text
A ≤p B
```

Meaning:

```text
A is polynomial-time reducible to B
```

If problem A can be reduced to problem B, then solving B efficiently also allows efficient solving of A.

Steps to Prove NP-Completeness:

1. Show that the problem belongs to NP.
2. Select a known NP-Complete problem.
3. Reduce the known NP-Complete problem to the new problem using polynomial-time transformation.
4. Conclude that the new problem is NP-Complete.

Importance of Reducibility:

- Used to prove NP-Completeness.
- Compares computational difficulty.
- Helps classify new problems.
- Provides a framework for complexity analysis.

Important Examination Points:

- NP-Complete problems are the hardest problems in NP.
- SAT was the first NP-Complete problem proved by Cook's Theorem.
- NP-Hard problems may not belong to NP.
- Polynomial-Time Reduction is denoted by ≤p.
- To prove NP-Completeness, first prove NP membership and then perform polynomial reduction.
- If one NP-Complete problem is solved in polynomial time, then all NP problems can be solved in polynomial time.

Frequently Asked Competitive Exam Facts:

```text
P ⊆ NP

NP-Complete = NP ∩ NP-Hard

First NP-Complete Problem:
SAT (Boolean Satisfiability)

Polynomial Reduction:
A ≤p B

Major NP-Complete Problems:
SAT
3-SAT
Clique
Vertex Cover
Hamiltonian Cycle
Subset Sum
Graph Coloring
TSP (Decision Version)

