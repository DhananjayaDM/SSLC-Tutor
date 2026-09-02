# Artificial Neural Networks
## Supervised Learning

Supervised Learning is a machine learning approach in which a model is trained using labeled data. In labeled data, each training example consists of input data along with its corresponding correct output. The objective of supervised learning is to learn the relationship between inputs and outputs so that it can accurately predict outputs for new unseen data.

The learning process involves providing the algorithm with a set of examples and allowing it to discover patterns, relationships, and rules from the data. Once training is completed, the model can make predictions for future instances.

Supervised learning problems are mainly classified into:

- Classification Problems
- Regression Problems

Classification involves predicting categorical outputs, whereas regression involves predicting continuous numerical values.

Common supervised learning algorithms include:

- Decision Trees
- Naïve Bayes
- K-Nearest Neighbor (KNN)
- Support Vector Machines (SVM)
- Neural Networks
- Linear Regression
- Logistic Regression

Applications:

- Email Spam Detection
- Medical Diagnosis
- Credit Risk Assessment
- Sentiment Analysis
- Image Classification
- Weather Forecasting

Advantages:

- High prediction accuracy when trained with quality data.
- Easy performance evaluation.
- Well-suited for classification and prediction tasks.

Disadvantages:

- Requires large amounts of labeled data.
- Data labeling can be expensive and time-consuming.
- Performance depends heavily on training data quality.

Time Complexity:

```text
Depends on Algorithm Used
```

Important Examination Points:

- Learns from labeled training data.
- Input and output data are known.
- Used for Classification and Regression.
- Common algorithms include Decision Tree, Naïve Bayes, KNN, and SVM.
- Examples: Spam Detection, Disease Prediction, House Price Prediction.

---

## Unsupervised Learning

Unsupervised Learning is a machine learning approach in which the model is trained using unlabeled data. Unlike supervised learning, no predefined output labels are available. The objective is to discover hidden patterns, structures, relationships, or groupings within the data.

The algorithm independently analyzes the data and identifies similarities and differences among data points. Unsupervised learning is particularly useful when labeled data is unavailable or expensive to obtain.

The main tasks of unsupervised learning are:

- Clustering
- Association Rule Mining
- Dimensionality Reduction

Clustering groups similar objects together, while association rule mining discovers relationships among variables.

Common unsupervised learning algorithms include:

- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Apriori Algorithm
- Principal Component Analysis (PCA)

Applications:

- Customer Segmentation
- Market Basket Analysis
- Recommendation Systems
- Social Network Analysis
- Data Compression
- Pattern Discovery

Advantages:

- Does not require labeled data.
- Useful for discovering hidden patterns.
- Suitable for exploratory data analysis.

Disadvantages:

- Difficult to evaluate results.
- Interpretation of clusters may be complex.
- Results depend on algorithm and parameters.

Time Complexity:

```text
Depends on Algorithm Used
```

Important Examination Points:

- Uses unlabeled data.
- No predefined target output.
- Main tasks are Clustering and Association Analysis.
- K-Means is the most popular clustering algorithm.
- Market Basket Analysis uses Association Rules.
- Data Mining frequently uses Unsupervised Learning.

---

## Reinforcement Learning

Reinforcement Learning is a machine learning approach in which an agent learns by interacting with an environment and receiving feedback in the form of rewards or penalties. The objective of the agent is to maximize cumulative rewards over time.

Unlike supervised learning, reinforcement learning does not use labeled examples. Instead, learning occurs through trial and error. The agent continuously observes its environment, takes actions, receives rewards, and adjusts its behavior accordingly.

The major components of Reinforcement Learning are:

- Agent
- Environment
- State
- Action
- Reward
- Policy

The agent learns an optimal policy that determines the best action to take in each state.

The learning cycle consists of:

```text
State
   ↓
Action
   ↓
Environment
   ↓
Reward
   ↓
New State
```

Common reinforcement learning algorithms include:

- Q-Learning
- SARSA
- Deep Q-Networks (DQN)
- Policy Gradient Methods

Applications:

- Robotics
- Self-Driving Cars
- Game Playing
- Resource Management
- Recommendation Systems
- Autonomous Systems

Advantages:

- Learns from interaction and experience.
- Suitable for dynamic environments.
- Can achieve highly optimized solutions.

Disadvantages:

- Requires large training time.
- Computationally expensive.
- Exploration may be risky in real-world environments.

Time Complexity:

```text
Depends on Environment and Learning Algorithm
```

Important Examination Points:

- Learning occurs through rewards and penalties.
- Agent interacts with environment.
- Goal is to maximize cumulative reward.
- Q-Learning is a popular Reinforcement Learning algorithm.
- Used in robotics, game playing, and autonomous systems.
- AlphaGo and autonomous vehicles use Reinforcement Learning.

---

## Comparison of Supervised, Unsupervised and Reinforcement Learning

| Feature | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|----------|-------------------|----------------------|------------------------|
| Training Data | Labeled | Unlabeled | Reward-Based |
| Goal | Predict Output | Discover Patterns | Maximize Reward |
| Feedback | Correct Answers Provided | No Feedback | Rewards and Penalties |
| Main Tasks | Classification, Regression | Clustering, Association | Sequential Decision Making |
| Example Algorithms | Decision Tree, SVM, KNN | K-Means, Apriori | Q-Learning, SARSA |
| Applications | Spam Detection, Prediction | Customer Segmentation | Robotics, Game Playing |

Important Examination Points:

- Supervised Learning → Labeled Data.
- Unsupervised Learning → Unlabeled Data.
- Reinforcement Learning → Reward-Based Learning.
- K-Means belongs to Unsupervised Learning.
- Q-Learning belongs to Reinforcement Learning.
- Classification is Supervised Learning.
- Clustering is Unsupervised Learning.
- Game Playing commonly uses Reinforcement Learning.