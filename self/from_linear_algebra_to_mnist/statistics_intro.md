# Statistics Intro

The variance of a dataset of vectors is the average of the squared distance of each vector to the mean vector of the dataset. A metric for measuring spread.

Given a dataset of vectors $\{x_1, \dots, x_N\}$ with mean $\bar{x}$, and for a single feature (scalar) with observations $x_1,\dots,x_N$ and mean $\bar{x}$:

$$
\text{Var}(X) = \frac{1}{N}\sum_{i=1}^N (x_i - \bar{x})^2
$$

Covariance is a metric for measuring how two things tends to move away from their averages in the same direction, in opposite direction, or randomly. Its unit is (units of $X$) * (units of $Y$).

For two features with observations $(x_i, y_i)$ and means $(\bar{x}, \bar{y})$:

$$
\text{Cov}(X, Y) = \frac{1}{N}\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})
$$

Correlation is covariance but scaled, so that it is unit-less and bounded between $-1$ and $1$ by defining. 

$$
\text{Corr}(X, Y) = \frac{\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^N (x_i - \bar{x})^2 \cdot \sum_{i=1}^N (y_i - \bar{y})^2}}
$$

$\text{Cov}(X, Y) = 0 \iff \text{Corr}(X, Y) = 0$

The covariance matrix is a matrix where, for centered data vectors $\tilde{x}_i = x_i - \bar{x}$:

$$
S[i, j] = \text{Cov}(i, j) = \frac{1}{N}\sum_{k=1}^N \tilde{x}_{k,i}\,\tilde{x}_{k,j}
$$