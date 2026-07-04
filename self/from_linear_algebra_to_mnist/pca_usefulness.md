# Principal Component Analysis

## PCA Usefulness

A PCA result is useful precisely when the eigenvalues are unevenly distributed, some are larger, others are lowers, and ideally nothing in between.

Data is observed through the lens of the PCA output which is the eigenvectors spectrum, which reports how the variance per feature of the data, distributed in the eigenvectors spectrum. 

Data has that property or don't. PCA is not forcing that distribution. PCA reveals the fact. Whether dimensionality reduction is going to pay off is decided by the data structure, PCA is the instrument that reads that structure.

With the raw data one can see the variance of each original feature, but not whether that variance is concentrated on some specific directions. PCA finds the directions that most concentrate the variance.

Variance in a direction $\mathbf{w}$ is $\mathbf{w}^T S \mathbf{w}$ which depends on the diagonals of $S$ (the variance per feature), but also on the cross terms (covariances between each pair of features)

$$\mathbf{w}^T S \mathbf{w} = \sum_i S_{ii} w_i^2 + \sum_{i \neq j} S_{ij} w_i w_j$$

The eigenvector basis has the property that the variance across a direction $\mathbf{w}$ depends only on the variance of the features individually, not cross terms, since it's diagonal.

$$\mathbf{w}^T D \mathbf{w} = \sum_i D_{ii} w_i^2$$

Orthogonal directions that are eigenvectors make the data under that new coordinate system to have no pairwise linear relation between them, in the sense that the covariance between any pair of features is $0$.