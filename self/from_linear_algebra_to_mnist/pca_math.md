## Problem It Solves:

There is a list of vectors $S = \{v_1, v_2, \dots, v_N\}$ of a $n$-dimensional space $A$. The question is: 

Find a pair of matrices $M = d \times n$, $M' = n \times d$, that minimizes the following sum:

$$\sum_{v \in S} \|v - M' M v\|^2$$

Here is the catch, because $n > d$, it is not possible to obtain $(M' M v = v)$, so the question is: 

Find the pair of matrices $M'$, $M$ that minimize that sum.

See that the span of $M'Mv$ will be vectors of dimension at most $d$.

## How to Solve It:

### Projection Linear Operator

Fix $M'$, from the least square problem is known that the quantity $\|v - M' (Mv)\|^2$ is minimized when $Mv$ is the vector such that $M'(Mv)$ is the projection of $v$ on the space spanned by $M'$.

The fact is that $M'M$ has to be the projection linear operator in the subspace spanned by $M'$, see that $M'$ fixes $M$ to ensure that, so I could replace $M'$ by any matrix whose column vectors span the same subspace that $M'$. The projection linear operator is determined by the subspace not by the basis used to span that space.

Due to the projection, the vectors $v$, $M'(Mv)$, $(v - M'Mv)$ form a triangle that's rectangle.

$$\|v\|^2 = \|M'Mv\|^2 + \|(v - M'Mv)\|^2$$

Because the sum $\|v\|^2$ is fixed, minimizing the original sum is equivalent to maximize the sum of $\|M'Mv\|^2$, and at this point what can be done.

If the columns of $M'$ are linearly dependent, let's say $d_1 < d$ is the rank of $M'$, then because what matters is the subspace spanned by $M'$ I can find a base made by $d_1$ linearly independent vectors whose remaining $d - d_1$ components are $0$. This is equivalent to solve the problem for $d_1$ instead of $d$.

For example, let's say $n = 3$, $d = 2$, and $M' = \begin{pmatrix}
  1 & 2  \\
  1 & 2 \\
\end{pmatrix}$, that subspace is the same as the one spanned by $M' = \begin{pmatrix}
  1 & 0  \\
  1 & 0 \\
\end{pmatrix}$, if using the latter, observe that the last $1 = 2 - 1$ coordinates, don't contribute to the sum that's being maximized $\|M'Mv\|^2$ because they are $0$. 

See that what's being summed per vector is its norm, which is the square of each coordinate, so if the last $(d - d_1)$ coordinates are $0$, that's the worst case, so having rank $d$ will be always better than something smaller. From this point assume that columns of $M'$ are linearly independent.

Always can be found an orthonormal basis that spans the same subspace as the column vectors of $M'$

### Optional

But because those are linearly independent, I can use the $QR$ factorization in particular.

From the $QR$ factorization is possible to find $Q'$ such that: $M' = Q'R$ and $M$ should be $R^{-1}(Q')^T$, see that $M' M = Q' (Q')^T$, so it is possible to use $Q'$ instead of $M$, and it has the plus that its columns are made of orthonormal vectors.


### Variance Computation

Let's assume that $M'$ is made up by orthonormal vectors. So that $M = (M')^T$.

The idea is that because $M M' = I_d$, and $\|M'Mv\|^2 = \langle M'Mv, M'Mv \rangle$, get that:

$$\begin{align}
\|M'Mv\|^2 &= (M'Mv)^T \cdot (M' M v) \\
           &= (v^T M^T (M')^T)(M' M v) \\
           &= (v^T M' M) (M' M v) \\
           &= v^T M' M v
\end{align}$$

And what to do from here?

Using trace operator, it's possible to continue, using the fact that if $B$, $C$ are such that $BC$ and $CB$ are square matrices (so that $tr$ operator is defined), then $\text{tr}(BC) = \text{tr}(CB)$.

With this, taking $B = v^T M'$, $C = Mv$

$$\begin{align}
v   &= n \times 1 \\
v^T &= 1 \times n \\
M'  &= n \times d \\
M   &= d \times n
\end{align}$$

$$\begin{align}
B &= v^T M' = 1 \times d \\
C &= Mv = d \times 1
\end{align}$$

$$\begin{align}
BC &= 1 \times 1 \\
CB &= d \times d
\end{align}$$

$$\begin{align}
\|M'Mv\|^2 &= \text{tr}(v^T M' M v),\ \text{because it's a } 1 \times 1 \text{ matrix.} \\
           &= \text{tr}(Mv v^T M')
\end{align}$$

This expression is better because now it can be reduced to:

$$\text{tr}(M (v v^T) M')$$

Now this is a sum over all the $v$'s:

$$\sum_{v \in S} \text{tr}(M (v v^T) M')$$

Because matrix multiplication is distributive on the left and on the right, and $\text{tr}$ operator is additive, i.e., $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$, get that:

$$\sum_{v \in S} \text{tr}(M (v v^T) M') = \text{tr}(M (\sum_{v \in S} v v^T) M')$$

And at this point the problem becomes maximize the following:

$\text{tr}(M S M')$ where $S$ is the matrix $(n \times n)$ obtained after the sum $v v^T$ is done over all the vectors $v$ is done.

$$\begin{align}
M &= d \times n \\
S &= n \times n \\
M' &= n \times d
\end{align}$$

$MSM'$ is a $d \times d$ matrix, from this point how to go on?

### Covariance Matrix.

This $S$ matrix has a statistical interpretation, $S[i, j]$ is the covariance between feature $i$ and feature $j$ (assuming features were centered at $0$, and scaled by $\frac{1}{N}$). 

$S$ is a real symmetric matrix, the spectral theorem allows ensuring that it has an orthogonal diagonalization. $S$ can be diagonalized, so let $S = RDR^{-1}$. $R$ is made by orthonormal columns, which is equivalent to $R^{-1} = R^T$.

If $W = (MR)$, then $MSM' = WDW^T$, because $D$ is a diagonal matrix, let $w_1, w_2, \dots, w_d$ the vector columns of $W^T$, and $d_1, d_2, \dots, d_n$ the diagonal values of $D$ then:

After doing, $\text{tr}(WDW^T)$ the quantity to maximize is:

$$\sum_{i=1}^d \sum_{j=1}^n d_j (w_{ij})^2$$

If $r_1, r_2, ..., r_n$ are the row vectors of $W^T$, then it's equivalent to maximize:

$$\sum_{j=1}^n d_j \left(\sum_{i=1}^d (w_{ij})^2\right) = \sum_{j=1}^n d_j \|r_j\|^2$$

$R$ is formed by orthonormal column vectors, see that the columns of $W^T = (MR)^T$, will be formed by orthonormal vectors, to see why it's enough to check that $W W^T = M R (MR)^T  = I_d$.

The reason is that if a matrix $A_{d \times n}$ is such that:

$A A^T = I_d$

Then this means that the dot product of the column vectors of $A^T$ with themselves is $1$, and with the other vectors is $0$, that's precisely what a set of vectors should hold to be orthonormal.

But that's an algebraic proof, $W^T = (MR)^T$, it has columns orthonormal if the columns of $R^T M^T$ are orthonormal.

$R$ is a square matrix that's orthonormal, and $M^T_{n \times d}$ contains orthonormal columns. What does $R$ does to the subspace generated by $M^T$.

A linear map that preserves lengths preserves angles also, but not vice versa, a linear map may preserve angles but not lengths for example $T(v) = 2v$.

Orthonormal square matrix transformations preserve lengths and angles, so the base vectors of $M^T$ will still be of the same length $1$, and have the same angle between them, i.e. orthogonality is preserved. The columns of $W^T$ will be precisely each column of $M$ with the $R^T$ transformation applied.

That means that the sum:

$$\sum_{j=1}^n \sum_{i=1}^d (w_{ij})^2 = d$$

Because there are $d$ vectors with length $1$.

And so:
$$\sum_{j=1}^n \|r_j\|^2 = d$$

There is other constraint on the $\|r_j\|$ and it's that $\|r_j\| \leq 1$.

This is because that matrix is made by $d$ column vectors, that matrix could be extended so that it's a full $n \times n$ matrix, without changing those vectors, in that case each $r_{ji}$ plus the additional entries, each squared, will sum $1$. So every $\|r_j\|$ is $\leq 1$. A square matrix with orthonormal columns is equivalent to a square matrix with orthonormal rows.

That with the constraint that they sum up to $d$, assuming that $d_1 \geq d_2 \geq d_3 \geq \dots \geq d_n \geq 0$, this is an optimization problem whose optimal solution is:

$$\|r_1\| = \|r_2\| = \dots = \|r_d\| = 1$$
$$\|r_{d+1}\| = \|r_{d+2}\| = \dots = \|r_n\| = 0$$

So basically $W^T$ will be like $\left[ \begin{array}{c} H \\  0 \end{array} \right]$, where $H$ is a $d \times d$ matrix made by orthonormal vectors.

Now:

$$W^T = R^T M^T = R^T M'$$

$$M' = R W^T$$

See that $R$ is the matrix whose columns are the eigenvectors of $S$. And because $W^T$ could be $\left[ \begin{array}{c} I \\  0 \end{array} \right]$, final result is interpret what is the result of $R W^T$.

Divide $R$ in $R_1, R_2$.

$R_1$ contains the first $d$ columns, i.e. the first $d$ eigenvectors and $R_2$ the remaining part, see that:

Because the structure of $W^T$, $R W^T$ is $R_1 H$, thus the subspace generated by $R W^T$ is the same as the one generated by $R_1 H$, but because $H$ is invertible, that means that the subspace generated by $R_1 H$ is the same as the one by $R_1$.

The interpretation of what $M'$ is doing is the following:

Start with $x$, $d$ dimensional, in the $d$ compressed space. Compressed in the sense that the process starts with $v$ $n$ dimensional, and $Mv$ reduces it to $d$ dimensional.

$M' (M v)$, i.e. $Mv$ is an at most $d$ dimensional subspace. The inputs of $M'$ are those vectors.

$W^T x = \begin{bmatrix} Hx \\ 0 \end{bmatrix}$ which does apply the $H$ linear map to $x$ and puts $(n-d)$ zeros at the end.

To make it $n$-dimensional, this $H$ linear map does not change the generated subspace.

Then $R$ changes the coordinates back to the standard base. But see that due to the $0$ at the end the contribution of the remaining $(n-d)$ eigenvectors are ignored.

## Conclusion from the Math

The subspace that minimizes the sum across all the vectors is the one generated by the largest $d$ eigenvectors of the matrix obtained after doing $\sum_{i = 1}^{N} v v^T$. Because of this, the compressed vectors are obtained by projecting $v$ onto this subspace. That's obtained by applying $M$ to $v$, and with this one what can be recovered is $M' M v$.

To apply PCA:

Find the covariance matrix, remember this is the covariance of the observed features, not the vectors, the vectors is a list of observed features. Diagonalize it, and start taking eigenvalues largest to smallest, looking at the cumulative ratio, until there is an elbow, or the curve flattens.

Basically, from this point there is no much contribution to the others dimensions, because the variance those are contributing is small compared to what's already taken.

Thus, see that a bad PCA is one where all the dimensions are contributing approximately the same variance.