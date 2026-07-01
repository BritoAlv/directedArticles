# QR Factorization

## Why It Is Needed?

If there is a vector $v$ $n \times 1$, and a matrix $M$ $n \times d$.

The thing is the following, how find among of all the vectors of the form $Mw$, i.e. the span of $M$, the one $x$ that minimizes the following:

$$\|v - Mx\|^2$$

This vector $x$ have to be the projection of $v$ in the subspace determined by $M$. That's a result.

The thing is that this projection can't be found simply by doing the dot product between $v$ and every column vector of $M$ because the column vectors of $M$ don't have to be necessarily be orthonormal.

So what to do?

## Gram Schmidt

Let's say that the vectors of $M$ are $v_1, v_2, \dots, v_d$.

There is an algorithm or procedure to find a set of orthonormal vectors that span the same subspace by doing the following:

Set $v_1 = \frac{v_1}{\|v_1\|}$
    $v_2 = \frac{v_2 - \langle v_2, v_1 \rangle v_1}{\|v_2 - \langle v_2, v_1 \rangle v_1\|}$
    $v_3 = \frac{v_3 - \langle v_3, v_1 \rangle v_1 - \langle v_3, v_2 \rangle v_2}{\|v_3 - \langle v_3, v_1 \rangle v_1 - \langle v_3, v_2 \rangle v_2\|}$
    $\dots$

The idea is that once is known a set of orthonormal vectors, to add a new one: 

Take $v$, linear independent to the vectors on the set, subtract from $v$ its projection in the subspace formed by the orthonormal vectors, normalize the resulting vector.

After doing that, a matrix $O$ $n \times d$ is obtained, i.e. $d$ vectors that are orthonormal, but what I'm missing is its relation with $M$.

## Factorization

See that those vectors span the same subspace as the ones from $M$, because at every step the operation was:

$$v_i = v_i - (\text{linear combination of the previous vectors})$$

That can be represented using linear transformations:

Scaling by $k$ the $i$-vector is encoded with the matrix:

$$I + (k - 1)e_i e_i^T$$

This is a $d \times d$ matrix, the thing about it is that, name its columns as $p_1, p_2, \dots, p_d$.

Fix a column let's say $p_i$, it is made by $p_{i1}, p_{i2}, \dots, p_{id}$, see that each of those coefficients $p_{ij}$, determines how much the vector $v_j$ will contribute to the transformed version of $v_i$.

It's like take $v_i$ will be mapped to a vector formed by $p_{ij}$ pieces of the vector $v_j$.

With this in mind, to build the transformation matrices:

Subtracting $v_i$ to $v_j$ can be done with the following matrix:

$e_1, e_2, \dots, e_d$, except that in the $j$-column put a $- \langle v_i, v_j \rangle$ in the $i$-row and a $1$ in the $j$-row.

See that all of those matrices are upper triangular. Start with $M$ and then do:

$$M R_1 R_2 \dots = M R = Q$$

The result is a matrix $R$ upper triangular, and a matrix $Q$ that spans the same subspace that $M$. With the additional property that the columns of $Q$ are made by orthonormal vectors.

Next, given $R^{-1}$:

$$M R R^{-1} = Q R^{-1}$$
$$M = Q R^{-1}$$

$R^{-1}$ exists because $R$ being upper triangular, means all of its vectors are linearly independent. 

It makes sense that it should exist, since one should be able to start with $Q$, apply all the linear transformations that were done and end up at $M$, in other words revert the process.

The issue here is that I don't know how to compute $R^{-1}$, leaving that aside, $Q$ is a matrix formed by $d$ column vectors ortonormals, and $R^{-1}$ is an upper triangular matrix.

In the least square problem the goal is finding the vector $x$ such that $\|v - Q R^{-1}x\|^2$ is minimized. 

Now that's equivalent to find the $w$ such that $w$ is the projection of $v$ in the subspace spanned by $Q$, which means solve the following:

$$w = \sum_{i=1}^d \langle q_i, v \rangle q_i$$

This has to be equal to $R^{-1}x$

$$w = R^{-1} x$$

$$x = Rw$$

So basically, $v$ is known, and with the $q_i$ is possible to compute $w$, and to compute $x$ what's needed is $R$, which is known. So that clears up that problem.

Now to find $R^{-1}$ is the inverse process, Start with $v_1, v_2, \dots, v_d$ and end up with $o_1, o_2, \dots, o_d$

How to recover $v_1$ from $o_1$, multiply $o_1$ by $\|v_1\|$,
How to recover $v_2$ from $\{o_2, o_1\}$

$$\begin{align}
o_2 &= \frac{v_2 - \langle v_2, o_1 \rangle o_1}{\|v_2 - \langle v_2, o_1 \rangle o_1\|} \\
v_2 &= o_2 \|v_2 - \langle v_2, o_1 \rangle o_1\| + \langle v_2, o_1 \rangle o_1
\end{align}$$

$$\begin{align}
o_3 &= \frac{v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2}{\|v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2\|} \\
v_3 &= o_3 \|v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2\| + \langle v_3, o_1 \rangle o_1 + \langle v_3, o_2 \rangle o_2
\end{align}$$

$v_2$ is defined by the second column of $R^{-1}$, in its first row, the pieces of $o_1$, To put $\langle v_2, o_1 \rangle$, in its second row is needed to put $\|v_2 - \langle v_2, o_1 \rangle o_1\|$ the piece relative to $o_2$.

Each of these indicate how many pieces of $o_i$ are needed to build the respective $v_i$, because to build $v_i$, only is needed $o_j$ with $j \leq i$ that makes sense of why the matrix should be upper triangular.

The matrix $R^{-1}$ will be given by:

$$\begin{align}
R^{-1}_{ii} &= \|v_i - \sum_{j=1}^{i-1} \langle v_i, o_j \rangle o_j\| \\
R^{-1}_{ji} &= \langle v_i, o_j \rangle, \quad j < i
\end{align}$$

## Finding the Projection Matrix in a Non-Orthogonal Basis

See that the least square problem is about a fixed subspace indicated by a matrix $M$, find the vector $x$, such that:

$$\|b - Mx\|^2$$

That expression is minimized. 

The solution is to find the vector $x$ such that $Mx$ is the projection of $b$ in that subspace.

$b$ is $n \times 1$, $M$ is $n \times d$, $M^T$ is $d \times n$, $x$ is $d \times 1$.

The challenge there is to find the $x$. If the columns of $M$ are orthonormal vectors, $x$ will be $M^T b$.

To see why that works, check:

$$\begin{align}
\langle b - Mx, Mx \rangle &= 0 \\
\langle b, Mx \rangle - \langle Mx, Mx \rangle &= 0 \\
b^T Mx - (x^T  M^T M x) &= 0 \\
b^T Mx &= x^T x
\end{align}$$

From this it should be the case that $b^T M = x^T \implies x = M^T b$ which is true.

Now what if the $M$ matrix is not made by orthonormal vectors, how to proceed when that is the case.

Write $M = QR$, where $Q$ is made by orthonormal vectors, and the subspace generated by $M$ is the same as
the one generated by $Q$, which means that:

To find the vector $x$ it should be simply $Q^T b$, but this is from the $Q$ orthonormal vectors columns point of view.

To convert them back to the $M$ basis, is needed to multiply it by $R^{-1}$, so that $x = R^{-1} Q^T b$.

See that $x = (R^{-1}Q^T) b$, and thus the projection matrix is $R^{-1}Q^T$. In terms of $M$ it is $(M^T M)^{-1}M^T$.

To see why it's enough with showing that: $(M^T M)x = M^Tb$, that comes from the dot product derivation $\langle b - Mx, Mx \rangle = 0$.
