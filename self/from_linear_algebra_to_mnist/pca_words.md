# Principal Component Analysis

## PCA in Words:

Start with some number of vectors, each with values for $m$ features, so that the shape of the vectors is:

$x = (x_1, x_2, \dots, x_m)$

Features are weight, height, etc. Having too much features may be a problem, so you set the task of find a way of represent the data using less features. Keep in mind that each feature is an axis on the coordinate system. From the features you have, you need a criterion that allows you to say I will keep this feature, and I will discard this one.

One criterion that can be used per feature is the variance of that feature, this means the average of the square differences between the feature value and the feature average. If before doing this to each feature value is subtracted the mean of the feature, i.e. the data is centered at $0$. What we are computing is the average of the sum of the squares of the projection of each vector onto that feature axis. Equivalently, the sum of the squares of the coordinates of the vector on that axis. Observe that the $\frac{1}{N}$ is constant across all the features.

So what one do is the following, compute the variances per feature, to obtain $m$ values and keep the features corresponding to the top $d$ values.

One issue with this naive approach is that the variances per feature could be roughly equal say $30, 30, 30$. So this approach is useless, what could be useful would be that the variances would be like $50, 60, 1$. See here is a good choice to discard the third axis, the other two contains most of the variance of the data.

The question is: 

There are features (axis) and observation of them, among all the linear transformation that preserve the total variance of the data. Is there any that distributes the total variance per feature in a way we hope (some features have small variance compared to others)?

Preserving the total variance is for being able to compare two different distributions, they should have the same total.

First, let's try to find what are the linear maps that preserve the variance?

If $A$ is a linear map, then transformed vectors will be $Ax$, and the total variance of the data is: 




This linear transformation can't change the shape of the data, so that the total variance is preserved, so it should be an orthogonal transformation, those only do rotation and reflection to the features (axis).

The problem comes to the following, fix a $d$, and ask: 

From all the orthogonal linear transformation, what's the one that maximizes the sum of the variances of its top $d$ features.

With linear algebra is proved some facts:

Compute the matrix that contains the covariance between each pair of features, this matrix has the property that all of its eigenvalues are real and non-negative.

The basis made by the eigenvectors is orthogonal and is the linear transformation we are looking for.

It holds that the variance of each transformed feature is the corresponding eigenvalue and the sum of the variance made by the top $d$ features is the biggest variance that can be achieved with any linear transformation.

Why that matrix solves the problem,

Compute the variance of each feature after is transformed by an orthogonal transformation.

$M \cdot v$, $M$ is the orthogonal transformation, $(n \times n)$

$v$ is each vector $(1 \times n)$

$Mv$ is a vector $(1 \times n) = \sum_{i = 1}^n \langle p_i, v \rangle p_i$, where $p_i$ are the column vectors of $M$, i.e. the new features axis.

The variance along that axis (feature) is $\sum_{j = 1}^m |\langle p_i, v_j \rangle|^2$. Which written in matrix form is: $\sum_{j = 1}^m |(p_i^T \cdot v_j)|^2$.

$$\begin{align}
(p_i^T \cdot v_j) \cdot (p_i^T \cdot v_j) &= (p_i^T \cdot v_j) \cdot (v_j^T \cdot p_i) \\
&= p_i^T \cdot V_j \cdot p_i
\end{align}$$

See that $V_j$ is a square matrix, but this being sum overall the $m$ vectors means:

$p_i^T \cdot S \cdot p_i$

$S$ is the covariance matrix of the features, i.e. $S[i, j] = \text{covariance}$ between feature $i$, and feature $j$.

When doing $M^T S M$ in each diagonal of this matrix is the term $p^T_i S p_i$. The total variance is thus $\text{tr}(M^T S M)$.

Remember the goal is to find the $M$ that maximizes the sum of the top largest values from the diagonal of that matrix.

Observe that minimize the reconstruction error, by the Pythagoras theorem turns out to be the same as maximizing the variance retained. 

More over the reason for using the variance as the criterion, is that is the equivalent to minimize the least square error, between the original vectors and the projected ones. The directions (axes) (features) in which project the vectors that best distribute the variance by concentrating it, is the one described before.

See that the projection transformation preserves the $0$ as the mean of the data. As $0$ isn't changed on any linear transformation.

Why use the variance from a statistical pov?

If the problem is stated from the idea of minimizing the reconstruction error, then maximizing variance is what happens to be the goal due to Pythagoras, that is mathematically proven, the statistical reasons are metrics, here is one:

1. Fix a direction, if a value per vector is to be kept in this direction to discriminate between different vectors. Those values obtained should have as much variance as possible, because variance is the average of the squared distance of those points with the mean.

One thing is what PCA optimizes, and other is what makes the result worth having.

Picking the same direction $d$ times does not make sense, because that would make the resulting data with rank one, that direction, the directions have to be linearly independent. Orthogonality ensures that directions are linearly independent, and provides a nice way of compute the variance in the new axis (features). What PCA wants is find the best $d$ dimensional subspace that maximizes the captured variance. Orthogonality allows find a new direction that's linearly independent to the previous ones.

A PCA result is useful precisely when the eigenvalues are unevenly distributed, some are larger, others are lowers, and ideally nothing in between.

Data is observed through the lens of the PCA output which is the eigenvectors spectrum, which reports how the variance of the data is distributed in the eigenvectors spectrum. Data has that property or don't. PCA is not forcing that distribution. PCA reveals the fact. Whether dimensionality reduction is going to pay off is decided by the data structure, PCA is the instrument that reads that structure.

With the raw data one can see the variance of each original feature, but not whether that variance is concentrated on some specific directions. PCA finds the directions that most concentrate the variance.

Variance in a direction $\mathbf{w}$ is $\mathbf{w}^T S \mathbf{w}$ which depends on the diagonals of $S$ (the variance per feature), but also on the cross terms (covariances between each pair of features)

$$\mathbf{w}^T S \mathbf{w} = \sum_i S_{ii} w_i^2 + \sum_{i \neq j} S_{ij} w_i w_j$$

The eigenvector basis has the property that the variance across a direction $\mathbf{w}$ depends only on the variance of the features individually, not cross terms, since it's diagonal.

$$\mathbf{w}^T D \mathbf{w} = \sum_i D_{ii} w_i^2$$

Orthogonal directions that are eigenvectors make the data under that new coordinate system to have no pairwise linear relation between them. But more than that, a feature can't be predicted using data from the others using least squares fitting, under that metric is not possible.

What means to my data to be represented with $0$ pairwise covariance features?

That knowing a feature does not give a linear guess in the least squares fitting sense of the other features. Again this is a metric. So the eigenvector basis is the one that has this property. When the data is observed from those directions is possibly to rule out that is not possible to linearly predict data from one direction using data from other direction.


## Greedy PCA

There is a greedy algorithm for maximizing the variance, find the direction (axis, feature that maximizes the variance), $v_1$.

Now find the next direction that maximizes the variance but is also orthogonal to $v_1$, call it $v_2$, and continue until $d$ directions has been found.

How ensure that's orthogonal to $v_1$, subtract from each feature vector, the projection on this direction, that will leave the orthogonal complement of that subspace, then with the remaining vectors, do the same did before.

Each vector $v_i$ will be mapped to $v_i - P_w v_i$

Where $P_w$ is the projection matrix on $w$.

See that is a linear transformation with matrix: $(I - P_w)$

$$v \mapsto (I - P_w)v$$

$$\langle w, (I - P_w)v \rangle$$
$$= \langle w, v - P_w v \rangle$$
$$= 0$$

To find the direction that maximizes the variance, use the previous proof when $d=1$. The algorithm will choose the eigenvalue corresponding to the largest eigenvalue, then find the orthogonal complement of this subspace and so on, the eigenvectors form an orthogonal base, so in the complementary subspace, the next eigenvector will be found. The greedy finds the optimal solution to the problem.