## Statistics POV

### Statistics Intro

The variance of a dataset of vectors is the average of the squared distance of each vector to the mean vector of the dataset. A metric for measuring spread.

$\text{Var}(X) = E( |X - E[X]|^2)$,

Covariance is a metric for measuring how two things tends to move away from their averages in the same direction, in opposite direction, or randomly. Its unit is (units of $X$) * (units of $Y$).

$\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])]$

Correlation is covariance but scaled, so that it is unit-less and bounded between $-1$ and $1$ by defining. 

$\text{Corr}(X, Y) = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X) \cdot \text{Var}(Y)}}$

Now $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2 \text{Cov}(X, Y)$

$\text{Cov}(X, Y) = 0 \iff \text{Corr}(X, Y) = 0$, then $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$

The covariance matrix is a matrix where $C[i, j] = \text{Cov}(i, j) = \text{Covariance}$ between features $i$, and $j$.

### Statistics in PCA

In the PCA context, it turns out that minimizing the error in the least square sense is equivalent to maximize the variance of the recovered features, assuming their mean is $0$.

The issue is how compute the variance of the recovered features, because there is correlation between them.

The total variance approach can't be used on the raw vectors, because the base is not orthonormal, the features are correlated, thus the variance can't be divided in independent directions.

That suggest the approach of finding any orthonormal basis, change the coordinates of the features to that base, and split the variance there,

Say the orthonormal basis is $v_1, v_2, \dots, v_p$, the transformed feature vectors will be, each vector in the dataset $x_i$ will be mapped to:

$$y_i = (v_1 \mid v_2 \mid \dots \mid v_p) x_i$$

Assume that mean is $0$, that means that the variance is: $\frac{1}{N}\sum_{i = 1}^N \|v_i\|^2$. In the PCA problem, the goal is maximize the variance of the decoded vectors, i.e. $\|M'Mv\|^2$, but see that because:

$$\begin{align}
\|M'Mv\|^2 &= (M' M v)^T (M'Mv) \\
           &= (v^T M^T M'^T) (M' M v) \\
           &= (v^T M^T) (M'^T M') (M v) \\
           &= (v^T M^T) (M v) \\
           &= \|Mv\|^2
\end{align}$$

This means that's equivalent to maximize the variance of the projected vectors onto the $d$-subspace. Keep in mind that $\frac{1}{N}$ is constant.

See that the variance of the $v_i$ vectors on a direction $w$ is:

$$V = w^T S w$$

If this $w$ is an eigenvector $w_i$ of the $S$ matrix, then:

$$\begin{align}
V &= \lambda_i \|w_i\|^2 \\
  &= \lambda_i
\end{align}$$

This means that the eigenvalues of the $S$ matrix are the variance of the vectors of the original set along each direction of the eigenbasis.

See that the $\text{tr}(MSM')$ is equal to the sum of the eigenvalues, i.e. the sum of the variances across each direction, this could be seen, as because $\|v\|^2 = \|w_1\|^2 + \dots + \|w_n\|^2$, so the total variance can be computed by summing the variances across each direction. This is a consequence that the eigenvectors form an orthonormal basis.

But the point here is that the ratio $\frac{\lambda_i}{\sum_{i = 1}^{n} \lambda_i}$ means how much variance is represented in that direction. The good thing about it is that being a ratio is units-free.

The nice thing about that decomposition is that the covariance between any pair of variables is $0$, and thus the variance of the sum of all the variables, can be computed as the sum of variance per dimension.