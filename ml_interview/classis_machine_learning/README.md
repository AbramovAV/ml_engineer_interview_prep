# Classic Machine Learning Algorithms
This section contains short summaries for classic ML algorithms, divided by groups.

## Supervised Learning

Supervised learning is a part of machine learning dedicated to training models on pairs **object** - **label**. Objects are characterized by a set of features, which are drawn from feature space $\mathbb{X}$. Labels are drawn from label space $\mathbb{Y}$. For supervised learning the given set of pairs looks like this: $X=\{(x_{1},y_{1}), ... (x_{N},y_{N})\}$, where $N$ is the number of object and labels in dataset.

### Linear Models

#### Linear Regression

Linear regression is a linear model that predicts continuous label based on a weighted sum of features. It can be written as a expicilt sum: $a(x) = w_0 + \sum_{i=1}^{D} w_ix_i$, where $D$ is the number of features for each object, $w_i$ is a weight of each feature, $x_i$ is a single feature; or as a matrix multiplication: $a(x) = w_0 + w \cdot x$, where $w$ is a weight vector and $x$ is a feature vector. In both equations $w_0$ is a bias term.

Weights can be calculated either by solving a matrix equation $w=(X^TX)^{-1}X^Ty$ or by minimizing loss function $\frac{1}{N}\sum_{i=1}^{N}(w \cdot x_i - y_i)^2 \rightarrow \min_{w}$ or $\frac{1}{N}\lVert Xw - y \rVert^2 \rightarrow \min_{w}$ (here bias term $w_0$ is included into weights $w$).

Added regularization helps to avoid overfitting. There are two mainly used methods: $L_1$ $\lVert w \rVert_1 = \sum_{i=1}^{D}|w_i|$ and $L_2$ $\lVert w \rVert_2 = \sum_{i=1}^{D}w_i^2$ regularization. Matrix equation transforms into $w=(X^TX + \lambda I)^{-1}X^Ty$ (only for $L_2$), where $\lambda$ is a hyperparameter that controls power of regularization.

#### Logistic Regression

The idea of Logistic Regression is to train a classifier that would predict a correct class probability. Probabilities of a trained model a obtained by applying a sigmoid function to predictions: $p(y=1|x) = \frac{1}{1-\exp(- w \cdot x)}$. The loss functions for Logistic Regression is $L(y,a(x)) = \sum_{i=1}^{N}\log(1+\exp(-y_i(w \cdot x_i)))$, where $a(x) = w \cdot x$

#### Support Vector Machines

SVM classifier creates an optimal hyperplain that divides two classes. To build this hyperplain, SVM utilizes only N closest points. SVM is a classifier that is defined by the following formula: $a(x) = sign(w \cdot x + w_0)$. Distance to the closest point is defined as $\frac{1}{\lVert w \rVert}$. Therefore, optimization task for SVM is:

$$\begin{cases}
      \frac{1}{2}\|w\|^2 + C \sum_{i=1}^{N}\xi_i \rightarrow \min_{w, w_0, \xi} \\
      y_i(w \cdot x + w_0) \ge 1 - \xi_i, i=1, \ldots, N\\
      \xi_i \ge 0, i=1, \ldots, N
    \end{cases}  $$

where $\xi$ is a parameter that penalizes if an object falls into $\frac{1}{\|w\|}$ margin aroung hyperplain, and $C$ is a coefficent that regulates how strongly classifier relies on training examples.

Equation above can be transformed into:

$$\frac{1}{2}\|w\|^2 + C\sum_{i=1}^{N}\max(0,1-y_i(w \cdot x + w_0)) \rightarrow min_{w, w_0}$$

### Metric Algorithms

Metric Algorithms predict a discrete or continuous label by taking a most frequent (for classification) or average (for regression) label.

#### K Nearest Neighbors

### Decision Trees

Decision Trees are non-linear algorithm, that contain a tree-like set of predicates where each predicate splits a given set into two parts $R_l$ and $R_r$ by comparing a selected feature $j$ with some threshold $t$: $R_l(j,t) = \{x | x_j < t\}$ and $R_r(j,t) = \{x | x_j \ge t\}$.

A criterion for selecting the best feature and threshold for split is formulated as: $Q(R_m, j, t) = H(R_m) - \frac{|\R_l|}{|\R_m|}H(R_l) - \frac{|\R_r|}{|\R_m|}H(R_r)$, where $|R|$ is the number of object that fall into each set, and $R_m$ is a full set of object before split.

#### Criterions for Regression

A main criterion is MSE: $H(R) = min_{t \in \mathbb{Y}} \frac{1}{|R|} \sum_{(x_i, y_i \in R)} (y_i - t)^2$, that can be transformed into $H(R) = \frac{1}{|R|} \sum_{(x_i, y_i \in R)} (y_i - \hat{y})$, where $\hat{y} = \frac{1}{|R|} \sum_{(x_i, y_i \in R)} y_i$.

#### Criterions for Classification

If each node of a tree returns a distibution of of class probabilities, than an optimal vector of probabilities would be a vector of class fractions $t = (p_1, \ldots, p_K)$ and a corresponding criterions are either Gini Criterion $H(R) = \sum_{i=1}^{K}p_i(1-p_i)$ or Enthropy Criterion $H(R) = \sum_{i=1}^{K}p_i\log{p_i}$.

#### ID3 Algorithm

Utilizes Enthropy Criterion to find an optimal split in node. Builds a tree until each leaf contains only objects of a single class, or while a next split gives a smaller criterion value.

#### C4.5

Utilizes Gain Ratio (Normalized Enthropy Criterion). Builds a tree until a minimum number of object in each leaf is met, then prunes a tree with *Error-Based Pruning* algorithm.

#### CART

Utilizes Gini Criterion. Prunes a tree with Cost-Complexity Pruning.

### Ensembles

#### Random Forest

#### Adaboost

#### Gradient Boosting

### Probabilistic Models

#### Naive Bayes Classifier

## Unsupervised Learning

### Clustering Models

#### KMeans

#### DBSCAN

#### Hierarchical Clustering

### Anomaly Detection

### Miscellaneous

#### Expectation-Maximization Algorithm

#### Principal Component Analysis

#### Singular Value Decomposition
