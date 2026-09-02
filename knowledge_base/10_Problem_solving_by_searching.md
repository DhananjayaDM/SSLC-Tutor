# Problem solving by searching
## Agents

An Agent is an entity that perceives its environment through sensors and acts upon that environment through actuators. In Artificial Intelligence, an agent is designed to perform actions that help achieve specific goals.

The behavior of an agent is determined by its perception of the environment and the actions it chooses in response. An intelligent agent continuously observes its surroundings, processes information, and makes decisions.

The components of an agent include:

- Sensors: Used to gather information from the environment.
- Actuators: Used to perform actions on the environment.
- Agent Function: Maps perceptions to actions.
- Performance Measure: Evaluates the success of the agent.

Types of Agents:

- Simple Reflex Agent
- Model-Based Agent
- Goal-Based Agent
- Utility-Based Agent
- Learning Agent

Applications:

- Robotics
- Autonomous Vehicles
- Virtual Assistants
- Expert Systems
- Intelligent Decision Systems

Important Examination Points:

- Agent = Sensors + Actuators.
- Rational Agent chooses the best possible action.
- Learning Agent improves performance through experience.
- Modern AI systems are based on Rational Agents.

---

## Problem and Solutions

Problem solving is one of the fundamental tasks of Artificial Intelligence. A problem is defined as a situation in which an intelligent system must determine a sequence of actions that transforms an initial state into a goal state.

A problem consists of:

- Initial State
- Goal State
- Operators or Actions
- State Space
- Path Cost

The process of solving a problem involves searching through the state space to find a path from the initial state to the goal state.

The quality of a solution is determined by:

- Correctness
- Optimality
- Completeness
- Efficiency

Applications:

- Route Planning
- Puzzle Solving
- Robotics
- Game Playing
- Scheduling

Important Examination Points:

- Initial State is the starting point.
- Goal State is the desired outcome.
- Operators transform one state into another.
- Search algorithms are used to find solutions.

---

## Breadth First Search (BFS)

Breadth First Search (BFS) is an uninformed search algorithm that explores nodes level by level. It expands all nodes at one depth before moving to nodes at the next depth level.

BFS uses a Queue data structure to maintain the order of exploration.

Characteristics:

- Complete Search Algorithm.
- Finds shortest path in unweighted graphs.
- Explores nodes level by level.
- Suitable for shallow solutions.

Advantages:

- Guaranteed to find a solution if one exists.
- Finds optimal solution in unweighted graphs.
- Simple implementation.

Disadvantages:

- High memory requirement.
- Slow for large state spaces.

Applications:

- Shortest Path Problems
- Network Broadcasting
- Social Networks
- Web Crawling

Time Complexity:

```text
O(b^d)
```

Space Complexity:

```text
O(b^d)
```

where:

```text
b = Branching Factor
d = Depth of Solution
```

Important Examination Points:

- BFS uses Queue.
- Complete and Optimal for unweighted graphs.
- Explores breadth before depth.

---

## Depth First Search (DFS)

Depth First Search (DFS) is an uninformed search algorithm that explores a branch completely before backtracking and exploring alternative branches.

DFS uses a Stack data structure or recursion.

Characteristics:

- Explores maximum depth first.
- Uses less memory than BFS.
- Suitable for deep search spaces.

Advantages:

- Lower memory requirement.
- Easy recursive implementation.
- Effective for traversal problems.

Disadvantages:

- Does not guarantee shortest path.
- May get trapped in deep branches.

Applications:

- Topological Sorting
- Cycle Detection
- Maze Solving
- Connectivity Testing

Time Complexity:

```text
O(b^m)
```

Space Complexity:

```text
O(bm)
```

where:

```text
b = Branching Factor
m = Maximum Depth
```

Important Examination Points:

- DFS uses Stack or Recursion.
- Not optimal.
- Used in Topological Sorting and Cycle Detection.

---

## A* Search

A* Search is a heuristic search algorithm that combines the advantages of Uniform Cost Search and Greedy Best First Search. It is one of the most efficient path-finding algorithms.

The evaluation function is:

```text
f(n) = g(n) + h(n)
```

where:

```text
g(n) = Actual cost from start node to current node

h(n) = Estimated cost from current node to goal
```

A* selects the node with the smallest f(n) value.

Characteristics:

- Informed Search Algorithm.
- Uses heuristics.
- Finds optimal solutions when heuristic is admissible.

Advantages:

- Efficient search.
- Optimal solution.
- Reduces search space.

Disadvantages:

- Requires memory.
- Depends on heuristic quality.

Applications:

- Route Finding
- Robotics
- Navigation Systems
- Game AI

Time Complexity:

```text
Exponential in worst case
```

Important Examination Points:

- Uses f(n)=g(n)+h(n).
- Optimal when heuristic is admissible.
- Most popular informed search algorithm.

---

## Bidirectional Search

Bidirectional Search is a search technique that simultaneously searches from the initial state and the goal state until the two searches meet.

Instead of searching from one direction only, the search effort is reduced by expanding nodes from both directions.

Characteristics:

- Two simultaneous searches.
- One search starts from initial state.
- Another search starts from goal state.

Advantages:

- Significant reduction in search space.
- Faster than BFS for many problems.

Disadvantages:

- Goal state must be known.
- Complex implementation.

Applications:

- Route Finding
- Network Search
- Path Planning

Time Complexity:

```text
O(b^(d/2))
```

Space Complexity:

```text
O(b^(d/2))
```

Important Examination Points:

- Searches from both ends.
- Often much faster than BFS.
- Two search frontiers meet in the middle.

---

## Greedy Best First Search

Greedy Best First Search is an informed search algorithm that expands the node that appears closest to the goal according to a heuristic function.

The evaluation function is:

```text
f(n) = h(n)
```

where:

```text
h(n) = Estimated distance to goal
```

Unlike A*, Greedy Search ignores the actual path cost.

Characteristics:

- Uses heuristic information.
- Goal-directed search.
- Focuses only on estimated distance.

Advantages:

- Fast search.
- Reduced exploration.

Disadvantages:

- Not always optimal.
- Can get stuck in local minima.

Applications:

- Route Planning
- Path Finding
- Artificial Intelligence Systems

Time Complexity:

```text
O(b^m)
```

Important Examination Points:

- Uses only h(n).
- Faster than uninformed search.
- Does not guarantee optimal solutions.

---

## Heuristic Functions

A Heuristic Function is an estimate of the cost required to reach the goal from a given state. It provides problem-specific knowledge that guides search algorithms toward promising solutions.

A heuristic function is represented as:

```text
h(n)
```

where:

```text
h(n) = Estimated cost from node n to goal
```

Good heuristics significantly reduce the search effort and improve performance.

Properties of Heuristics:

- Domain-specific.
- Guides search process.
- Improves efficiency.

Types of Heuristics:

- Admissible Heuristic
- Consistent Heuristic
- Informed Heuristic

An Admissible Heuristic never overestimates the true cost to the goal.

Applications:

- A* Search
- Greedy Search
- Game Playing
- Robotics
- Navigation Systems

Advantages:

- Reduces search space.
- Faster problem solving.
- Supports intelligent decision making.

Disadvantages:

- Difficult to design.
- Poor heuristics may reduce performance.

Important Examination Points:

- h(n) estimates distance to goal.
- Admissible Heuristic never overestimates.
- A* uses g(n) + h(n).
- Greedy Search uses only h(n).
- Heuristics are central to informed search algorithms.