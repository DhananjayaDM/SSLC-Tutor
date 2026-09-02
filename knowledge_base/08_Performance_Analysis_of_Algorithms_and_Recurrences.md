# Performance Analysis of Algorithms and Recurrences
## Time and Space Complexities

Time Complexity and Space Complexity are measures used to evaluate the efficiency of an algorithm. They help in estimating how an algorithm performs as the size of the input increases.

Time Complexity refers to the amount of time required by an algorithm to execute as a function of the input size. It does not represent actual execution time in seconds but rather the growth rate of the number of operations performed. Time complexity is important because it helps compare different algorithms and choose the most efficient one for a given problem.

Common time complexities are:

```text
O(1)       Constant Time
O(log n)   Logarithmic Time
O(n)       Linear Time
O(n log n) Linearithmic Time
O(n²)      Quadratic Time
O(n³)      Cubic Time
O(2ⁿ)      Exponential Time
O(n!)      Factorial Time
```

Space Complexity refers to the amount of memory required by an algorithm during its execution. It includes memory required for variables, data structures, function calls, recursion stacks, and auxiliary storage.

Space complexity consists of:

```text
Input Space
+
Auxiliary Space
```

Algorithms that require less memory are generally preferred for large-scale applications. However, in many cases there is a trade-off between time and space efficiency known as the Time-Space Tradeoff.

Time and space complexity analysis is essential in algorithm design because it helps predict performance, optimize resource utilization, and compare alternative solutions. Competitive examinations frequently ask questions involving calculation, comparison, and interpretation of complexity measures.

Important Examination Points:

- Time Complexity measures execution growth with input size.
- Space Complexity measures memory growth with input size.
- Best Case, Average Case, and Worst Case complexities are often evaluated.
- Constant and logarithmic complexities are considered highly efficient.
- Exponential and factorial complexities are generally inefficient for large inputs.

---

## Asymptotic Notation

Asymptotic Notation is a mathematical tool used to describe the growth rate of an algorithm's time or space complexity as the input size approaches infinity. It provides a machine-independent way of comparing algorithms.

Asymptotic analysis focuses on the dominant term of a complexity expression while ignoring lower-order terms and constant factors. This allows algorithm performance to be analyzed independently of hardware and implementation details.

The three major asymptotic notations are Big-O, Big-Omega, and Big-Theta.

Big-O Notation represents the upper bound of an algorithm. It describes the maximum amount of time or space required by the algorithm in the worst-case scenario.

Examples:

```text
O(1)
O(log n)
O(n)
O(n²)
```

Big-Omega Notation represents the lower bound of an algorithm. It describes the minimum amount of work performed by the algorithm in the best-case scenario.

Examples:

```text
Ω(1)
Ω(log n)
Ω(n)
```

Big-Theta Notation represents the exact bound when both the upper and lower bounds are the same. It indicates the actual growth rate of the algorithm.

Examples:

```text
Θ(n)
Θ(n log n)
Θ(n²)
```

Other asymptotic notations include:

```text
Little-o Notation
Little-omega Notation
```

These are used mainly in advanced algorithm analysis and theoretical computer science.

Asymptotic notation helps determine scalability, compare algorithms, analyze efficiency, and predict performance for very large inputs.

Important Examination Points:

- Big-O represents Worst Case.
- Big-Omega represents Best Case.
- Big-Theta represents Tight Bound.
- Ignore constants and lower-order terms.
- Most competitive exams focus on Big-O analysis.

Common Examples:

```text
Linear Search      O(n)
Binary Search      O(log n)
Bubble Sort        O(n²)
Merge Sort         O(n log n)
Quick Sort Avg     O(n log n)
Quick Sort Worst   O(n²)
```

---

## Recurrence Relations

A Recurrence Relation is an equation that defines a problem or algorithm in terms of smaller instances of itself. Recurrence relations are widely used to analyze recursive algorithms.

Instead of expressing the complexity directly, recursive algorithms are represented by recurrence equations that describe how the problem size decreases at each step.

General Form:

```text
T(n) = Cost of Smaller Subproblems
       + Cost of Current Work
```

Examples:

```text
T(n) = T(n-1) + 1
```

Represents a simple recursive process.

```text
T(n) = T(n/2) + 1
```

Represents a divide-and-conquer algorithm.

```text
T(n) = 2T(n/2) + n
```

Represents algorithms such as Merge Sort.

Recurrence relations help determine the time complexity of recursive algorithms by expressing computation in terms of smaller subproblems.

Several techniques are used to solve recurrence relations:

1. Substitution Method
2. Iteration Method
3. Recursion Tree Method
4. Master Theorem

The Master Theorem is one of the most important tools for solving divide-and-conquer recurrences.

General Form:

```text
T(n) = aT(n/b) + f(n)
```

where:

```text
a = Number of Subproblems
b = Reduction Factor
f(n) = Cost of Dividing and Combining
```

Examples:

```text
Binary Search

T(n) = T(n/2) + 1

Complexity:
O(log n)
```

```text
Merge Sort

T(n) = 2T(n/2) + n

Complexity:
O(n log n)
```

```text
Tower of Hanoi

T(n) = 2T(n-1) + 1

Complexity:
O(2ⁿ)
```

Recurrence relations are fundamental in the analysis of recursive algorithms, divide-and-conquer techniques, dynamic programming, and advanced algorithm design.

Important Examination Points:

- Used to analyze recursive algorithms.
- Expresses a problem in terms of smaller instances.
- Merge Sort recurrence: T(n)=2T(n/2)+n.
- Binary Search recurrence: T(n)=T(n/2)+1.
- Master Theorem is the most frequently asked method.
- Widely appears in NET, SET, KSET, GATE, and University examinations.