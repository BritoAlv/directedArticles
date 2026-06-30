## QR Factorization

If there is a vector $v$ $n \times 1$, and a matrix $M$ $n \times d$.

The thing is the following, how find among all the vectors of the form $Mw$, i.e. the span of $M$, the one $x$ that minimizes the following:

$$\|v - Mx\|^2$$

Is known that this $x$ vector should be precisely the projection of $v$ in the subspace determined by $M$.

The thing is that this projection can't be found simply by doing the dot product between $v$ and every column vector of $M$ because the column vectors of $M$ don't have to be necessarily be ortonormal.

So what to do?

Let's say that the vectors of $M$ are $v_1, v_2, \dots, v_d$, is possible to find a set of ortonormal vectors that span the same subspace by doing the following:

Set $v_1 = \frac{v_1}{\|v_1\|}$
    $v_2 = \frac{v_2 - \langle v_2, v_1 \rangle v_1}{\|v_2 - \langle v_2, v_1 \rangle v_1\|}$
    $v_3 = \frac{v_3 - \langle v_3, v_1 \rangle v_1 - \langle v_3, v_2 \rangle v_2}{\|v_3 - \langle v_3, v_1 \rangle v_1 - \langle v_3, v_2 \rangle v_2\|}$
    $\dots$

That's known as the Gram-Schmidt process. The idea is that one that is known a set of ortonormal vectors, to add a new one, substract from it its projection in the subspace formed by the ortonormal vectors.

After doing that I obtain a matrix $O$ $n \times d$, ie $d$ vectors that are ortonormal, but what I'm missing is its relation with $A$.

See that those vectors span the same subspace as the ones from $M$, because at every step the operation was:

$$v_i = v_i - (\text{linear combination of the previous vectors})$$

That can be represented using linear transformations:

Scaling by $k$ to the $i$-vector is with a matrix like:

$$I + (k - 1)e_i e_i^T$$

This is a $d \times d$ matrix, the thing about it is that,

it has columns $p_1, p_2, \dots, p_d$,

Fix a column let's say $p_i$, its made by $p_{i1}, p_{i2}, \dots, p_{id}$, see that each of those coefficients $p_{ij}$, determines how much the vector $v_j$ will contribute to the transformed version of $v_i$. It's like take $v_i$ will be mapped to a vector formed by $p_{ij}$ pieces of the vector $v_j$.

With this in mind is easy to build the transformation matrices.

Substracting $v_i$ to $v_j$ can be done with the following matrix:

$e_1, e_2, \dots, e_d$, except that in the $j$-column put a $-1$ in the $i$-row and a $1$ in the $j$-row.

See that all of those matrices are upper triangular.Start with $A$ and then do:

$$A M_1 M_2 \dots = A R = Q$$

The result is a matrix $R$ upper triangular, and a matrix $Q$ that spans the same subspace that $A$, with the additional property that the columns of $Q$ are made by ortonormal vectors.

Next, given $R^{-1}$:

$$A R R^{-1} = Q R^{-1}$$
$$A = Q R^{-1}$$

$R^{-1}$ exist because $R$ being upper triangular, means all of its vectors are linearly independent, but it makes sense that it should exist, since one should be able to start with $Q$, apply all the linear transformations that were done and end up at $A$, basically revert the process.

The issue here is that I don't know how to compute $R^{-1}$, leaving that aside $Q$ is a matrix formed by $d$ column vectors ortonormals, and $R^{-1}$ is an upper triangular matrix.

In the least square problem the goal is find the vector $x$ such that $\|v - Q R^{-1}x\|^2$ is minimized, now that's equivalent to find the $w$ such that $w$ is the projection of $v$ in the subspace spanned by $Q$, which means solve the following:

$$w = \sum_{i=1}^d \langle q_i, v \rangle q_i$$

This has to be equal to $R^{-1}x$

$$w = R^{-1} x$$

$$x = Rw$$

So basically, because there is $v$, and with the $q_i$ is possible to compute $w$, and to compute $x$ what's needed is $R$, which is known. So that clears up that problem.

Now to find $R^{-1}$ is the inverse process, Start with $v_1, v_2, \dots, v_d$ and end up with $o_1, o_2, \dots, o_d$

How to recover $v_1$ from $o_1$, multiply $o_1$ by $\|v_1\|$,
How to recover $v_2$ from $\{o_2, o_1\}$

$$o_2 = \frac{v_2 - \langle v_2, o_1 \rangle o_1}{\|v_2 - \langle v_2, o_1 \rangle o_1\|}$$

$$v_2 = o_2 \|v_2 - \langle v_2, o_1 \rangle o_1\| + \langle v_2, o_1 \rangle o_1$$

$$o_3 = \frac{v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2}{\|v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2\|}$$

$$v_3 = o_3 \|v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2\| + \langle v_3, o_1 \rangle o_1 + \langle v_3, o_2 \rangle o_2$$

$v_2$ is defined by the second column of $R^{-1}$, in its first row, the pieces of $o_1$, To put $\langle v_2, o_1 \rangle$, in its second row is needed to put $\|v_2 - \langle v_2, o_1 \rangle o_1\|$ the piece relative to $o_2$.

Each of these indicate how many pieces of $o_i$ are needed to built the respective $v_i$, because to build $v_i$, only is needed $o_j$ with $j \leq i$ that makes sense of why the matrix should be upper triangular.

The matrix $R^{-1}$ will be given by:

$$R^{-1}_{ii} = \|v_i - \sum_{j=1}^{i-1} \langle v_i, o_j \rangle o_j\|$$
$$R^{-1}_{ji} = \langle v_i, o_j \rangle, \quad j < i$$

## Finding the Projection Matrix in a Non Ortogonal Basis

See that the least square problem is about a fixed subspace indicated by a matrix $A$, find the vector $x$, such that:

$Ax$ is the projection of $b$ in that subspace.

$$\|b - Ax\|^2$$

$b$ is $n \times 1$,
$A$ is $n \times d$,
$A^T$ is $d \times n$,
$x$ is $d \times 1$,

So the challenge there is to find the $x$, which is easy to do if the columns of $A$ are ortonormal vectors,

$x$ will be $A^T b$

And the reason of why that works, is that to check:

$$\langle b - Ax, Ax \rangle = 0$$
$$\langle b, Ax \rangle - \langle Ax, Ax \rangle = 0$$
$$b^T Ax - (x^T A^T A x) = 0$$
$$b^T Ax = x^T x$$

From this it should be the case that $b^T A = x^T \implies x = A^T b$ which is true.

Now what if the $A$ matrix is not made by ortonormal vectors, how to proceed when that is the case.

Write $A = QR$, where $Q$ is made by ortonormal vectors, and the subspace generated by $A$ is the same as
the one generated by $Q$, which means that:

To find the vector $x$ it should be simply $Q^T b$, but this is from the $Q$ ortonormal vectors columns point of view.

To convert them back to the $A$ basis, Is needed to multiply it by $R^{-1}$, so that $x = R^{-1} Q^T b$.

See that $x = (R^{-1}Q^T) b$, and thus the projection matrix is $R^{-1}Q^T$. In terms of M is (M^T M)^{-1}M^T.

To see why it's enough with showing that: (M^T * M)x = M^Tb, That comes from the dot product derivation <b - Mx, Mx> = 0.