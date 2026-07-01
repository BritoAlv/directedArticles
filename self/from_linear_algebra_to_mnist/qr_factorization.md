# QR Factorization

## Why It Is Needed?

If there is a vector $v$ $n \times 1$, and a matrix $M$ $n \times d$.

The thing is the following, how find among of all the vectors of the form $Mw$, i.e. the span of $M$, the one $x$ that minimizes the following:

$$\|v - Mx\|^2$$

This vector $x$ have to be the projection of $v$ in the subspace determined by $M$. That's a result.

The thing is that this projection can't be found simply by doing the dot product between $v$ and every column vector of $M$ because the column vectors of $M$ don't have to be necessarily be orthonormal.

So what to do?

Find an orthonormal basis that spans the same subspace as $M$, find the projection in that space using that orthonormal basis, and then convert back to the coordinates of $M$. 

Is needed a way of finding the orthonormal basis from $M$, that's the purpose of the $QR$ factorization. 

## Gram Schmidt

Let's say that the vectors of $M$ are $v_1, v_2, \dots, v_d$.

There is an algorithm or procedure to find a set of orthonormal vectors that span the same subspace by doing the following:

Set $q_1 = \frac{v_1}{\|v_1\|}$
    $q_2 = \frac{v_2 - \langle v_2, q_1 \rangle q_1}{\|v_2 - \langle v_2, q_1 \rangle q_1\|}$
    $q_3 = \frac{v_3 - \langle v_3, q_1 \rangle q_1 - \langle v_3, q_2 \rangle q_2}{\|v_3 - \langle v_3, q_1 \rangle q_1 - \langle v_3, q_2 \rangle q_2\|}$
    $\dots$

The idea is that once is known a set of orthonormal vectors, to add a new one: 

Take $v$, linear independent to the vectors on the set, subtract from $v$ its projection in the subspace formed by the orthonormal vectors, and normalize the resulting vector.

After doing that, a matrix $Q$ $n \times d$ is obtained, i.e. $d$ vectors that are orthonormal. 

How to recover $v_1$ from $q_1$, multiply $q_1$ by $\|v_1\|$,
How to recover $v_2$ from $\{q_2, q_1\}$

$$\begin{align}
q_2 &= \frac{v_2 - \langle v_2, q_1 \rangle q_1}{\|v_2 - \langle v_2, q_1 \rangle q_1\|} \\
v_2 &= q_2 \|v_2 - \langle v_2, q_1 \rangle q_1\| + \langle v_2, q_1 \rangle q_1
\end{align}$$

$$\begin{align}
q_3 &= \frac{v_3 - \langle v_3, q_1 \rangle q_1 - \langle v_3, q_2 \rangle q_2}{\|v_3 - \langle v_3, q_1 \rangle q_1 - \langle v_3, q_2 \rangle q_2\|} \\
v_3 &= q_3 \|v_3 - \langle v_3, q_1 \rangle q_1 - \langle v_3, q_2 \rangle q_2\| + \langle v_3, q_1 \rangle q_1 + \langle v_3, q_2 \rangle q_2
\end{align}$$

See that those vectors $q_1, q_2, ...$ span the same subspace as the ones from $M$, because at every step the operation was:

$$q_i = v_i - (\text{linear combination of the previous vectors})$$

Those steps can be represented using linear transformations:

Scaling by $k$ the $i$ basis vector is encoded with the matrix:

$$I + (k - 1)e_i e_i^T$$

This is a $d \times d$ matrix, the thing about it is that, name its columns as $p_1, p_2, \dots, p_d$.

Fix a column let's say $p_i$, it is made by $p_{i1}, p_{i2}, \dots, p_{id}$, see that each of those coefficients $p_{ij}$, determines how much the vector $v_j$ will contribute to the transformed version of $v_i$.

It's like take $v_i$ will be mapped to a vector formed by $p_{ij}$ pieces of the vector $v_j$.

With this in mind, to build the transformation matrices:

Subtracting the projection of $v_j$ on $q_i$ can be done with the following matrix:

$e_1, e_2, \dots, e_d$, except that in the $j$-column put a $- \langle v_j, q_i \rangle$ in the $i$-row and a $1$ in the $j$-row.

See that all of those matrices are upper triangular (because every step uses only vectors from previous steps). Start with $M$ and then do:

$$M R_1 R_2 \dots = M R^{-1} = Q$$

See that the linear transformation are applied on the right, instead of the left, like one usually do, this is to ensure that $(MR_1)$ has the desire effect on the columns of $M$ and so on.

Knowing $Q$ and the column vectors of $M$ $v_1, v_2, ..., v_d$, one can define $R^{-1}$ by:

$$\begin{align}
R^{-1}_{ii} &= \|v_i - \sum_{j=1}^{i-1} \langle v_i, q_j \rangle q_j\| \\
R^{-1}_{ji} &= \langle v_i, q_j \rangle, \quad j < i
\end{align}$$

So that $MR^{-1} = Q$. 

See that this matrix have inverse, it is enough with checking that its diagonal entries are nonzero because it is upper triangular. Those diagonal entries are the norm of linear independent vectors, which implies none of them is $0$.

Each of these indicate how many pieces of $q_i$ are needed to build the respective $v_i$, because to build $v_i$, only is needed $q_j$ with $j \leq i$ that makes sense of why the matrix that does that linear transformation should be upper triangular.

## Factorization

The result is a matrix $R$ upper triangular, and a matrix $Q$ that spans the same subspace that $M$. With the additional property that the columns of $Q$ are made by orthonormal vectors.

Next, given $R^{-1}$:

$$M R R^{-1} = Q R^{-1}$$
$$M = Q R^{-1}$$

$Q$ is a matrix formed by $d$ column vectors orthonormals, and $R^{-1}$ is an upper triangular matrix.

## Least Squares.

In the least square problem the goal is finding the vector $x$ such that $\|v - Q R^{-1}x\|^2$ is minimized. 

$v$ is a $n * 1$ vector. $Q$ is an $n * d$ matrix whose columns $q_1, ..., q_d$ are orthonormal basis vectors.

The projection of $v$ on each of the $q_i$ vectors $q_i$ is:

$\langle q_i, v \rangle = q_i^T v$

The coordinates of the projection of $v$ in the subspace formed by the $q$ vectors is:

$$
w = 
\begin{bmatrix}
\langle q_1, v \rangle \\
\langle q_2, v \rangle \\
\vdots \\
\langle q_d, v \rangle
\end{bmatrix} = Q^T v
\quad (  d \times 1)  
$$

The projection vector on that subspace is $\hat{v} = \sum_{i = 1}^d \langle q_i, v \rangle q_i$, or equivalently $Qw$.



From that we get that: 

$$ Qw = QR^{-1}x$$

Because $Q$ has orthonormal columns, then $Q^T Q = I$, multiply both sides by $Q^T$:

$$w = R^{-1} x$$

$$x = Rw$$

Finally, $x = RQ^Tv$.

## Finding the Projection Matrix in a Non-Orthogonal Basis

See that the least square problem is about a fixed subspace indicated by a matrix $M$, find the vector $x$, such that:

$$\|b - Mx\|^2$$

Is minimized. 

The solution is to find the vector $x$ such that $Mx$ is the projection of $b$ in that subspace.

$b$ is $n \times 1$, $M$ is $n \times d$, $M^T$ is $d \times n$, $x$ is $d \times 1$.

To solve that issue one necessary condition is check that $\langle b - Mx, Mx \rangle =0$, but this is not enough, since the projection vector should be orthogonal to all the vectors on the subspace spanned by $M$, not one of them, $Mx$ in this case. 

Let $m_1, m_2, ..., m_d$ the column vectors of $M$, the enough condition is that the $d$ equations, $\langle b - Mx, m_i \rangle =0$ are satisfied by some $x$.

Which can be written in matrix form as $(b - Mx)^T M = 0$, or equivalently $M^T (b - Mx) = 0$, from this is obtained that:

$$M^T b = M^T M x$$

If somehow can be proven that $M^T M$ has inverse then the solution is $x = (M^T M)^{-1} M^T b$. To show that the inverse always exist:

$$
\begin{align}
M^T M x &= 0 \\
x^T M^T M x &= 0 \\
(Mx)^T (Mx) &= 0 \\
|Mx|^2 &= 0
\end{align}
$$

Because columns of $M$ are linearly independent the only solution to that equation is $x = 0$.

From the previous analysis if $M = QR^{-1}$, then $x = RQ^Tb$, and from this analysis we get other expression for $x$ written only in terms of $M$.

It should be the case that:

$$(M^T M)^{-1} M^T = R Q^T$$
