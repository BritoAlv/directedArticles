# Linear Regression

Given pairs of the form $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$, where $x_i$ are on $R^d$, and $y_i$ are points on $R$, the goal is find a function $F$:

1. $F : R^d \to R$,
2. $F$ linear, this means of the form $F(x) = w^T x$, $|w| = 1$
3. $F$ should minimize the error sum $\sum_{x_i \in X} |w^T x - y_i|^2$

Put all the $y_i$ on a vector $y$, put all the $x_i$ on a matrix $X$, so that the error sum becomes:

The vector $w^T X$ is the result of applying $w^T$ to each column vector of a matrix $X$ formed by putting each vector $x_i$ in a column

$$
|w^T X - y|^2 = |X^T w - y|^2
$$

the solution to this problem is that $w$ should be the coordinate vector of the projection of $y$ in the subspace spanned by the column vectors of $w^T$.