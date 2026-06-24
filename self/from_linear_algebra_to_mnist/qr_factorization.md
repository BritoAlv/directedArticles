## QR Factorization

If there is a vector $v$ $n \times 1$, and a matrix $M$ $n \times d$.

The thing is the following, if we set to find among all the vectors of the form $Mw$, ie the span of $w$, the one $x$ that minimizes the following:

$$\|v - Mx\|^2$$

Is known that this $x$ vector should be precisely the projection of $v$ in the subspace determined by $M$.

The thing is that this projection can't be found simply by doing the dot product between $v$ and every column vector of $M$ because the column vectors of $M$ don't have to be necessarily be ortonormal.

So what to do?

Let's say that the vectors of $M$ are $v_1, v_2, \dots, v_d$, is possible to find a set of ortonormal vectors that span the same subspace by doing the following:

Set $v_1 = \frac{v_1}{\|v_1\|}$
    $v_2 = \frac{v_2 - \langle v_2, v_1 \rangle v_1}{\|v_2\|}$
    $v_3 = \frac{v_3 - \langle v_3, v_1 \rangle v_1 - \langle v_3, v_2 \rangle v_2}{\|v_3\|}$
    $\dots$

That's known as the Gram-Schmidt process. The idea is that one that is known a set of ortonormal vectors, to add a new one, substract from it its projection in the subspace formed by the ortonormal vectors.

After doing that I obtain a matrix $O$ $n \times d$, ie $d$ vectors that are ortonormal, but what I'm missing is its relation with $A$.

See that those vectors span the same subspace as the ones from $M$, because at every step the operation was:

$$v_i = v_i - (\text{linear combination of the previous vectors})$$

That can be represented using linear transformations:

Scaling by $k$ to the $i$-vector is with a matrix like:

$$I + (k - 1)e_i$$ 

This is a $d \times d$ matrix, the thing about it is that,

it has columns $p_1, p_2, \dots, p_d$,

Fix a column let's say $p_i$, its made by $p_{i1}, p_{i2}, \dots, p_{id}$, see that each of those coefficients $p_{ij}$, determines how much the vector $v_j$ will contribute to the transformed version of $v_i$. It's like take $v_i$ will be mapped to a vector formed by $p_{ij}$ pieces of the vector $v_j$.

With this in mind is easy to build the transformation matrices.

Substracting $v_i$ to $v_j$ can be done with the following matrix:

$e_1, e_2, \dots, e_d$, except that in the $j$-column put a $-1$ in the $i$-row and a $1$ in the $j$-row.

See that all of those matrices are upper triangular, so we can start with $A$ and then do:

$$A M_1 M_2 \dots = A R = Q$$

We end up with a matrix $R$ upper triangular, and a matrix $Q$ that spans the same subspace that $A$, with the additional property that the columns of $Q$ are made by ortonormal vectors.

Next, given $R^{-1}$:

$$A R R^{-1} = Q R^{-1}$$
$$A = Q R^{-1}$$

$R^{-1}$ exist because $R$ being upper triangular, means all of its vectors are linearly independent, but it makes sense that it should exist, since we should be able to start with $Q$, apply all the linear transformations we did and end up at $A$, basically revert the process.

The issue here is that I don't know how to compute $R^{-1}$, leaving that aside $Q$ is a matrix formed by $d$ column vectors ortonormals, and $R^{-1}$ is an upper triangular matrix.

In the least square problem we that we need to find the vector $x$ such that $\|v - Q R^{-1}x\|^2$ is minimized, now that's equivalent to find the $w$ such that $w$ is the projection of $v$ in the subspace spanned by $Q$, which means solve the following:

$$w = \sum_{i=1}^d \frac{\langle q_i, v \rangle}{\|v_i\|} q_i$$ 

This has to be equal to $R^{-1}x$

$$w = R^{-1} x$$

$$x = Rw$$

So basically, because we have $v$, and the $q_i$ we can compute $w$, and to compute $x$ what's needed is $R$, which is known. So that clears up that problem.

Now to find $R^{-1}$ is the inverse process, let's say we start with $v_1, v_2, \dots, v_d$ and end up with $o_1, o_2, \dots, o_q$

How to recover $v_1$ from $o_1$, multiply $o_1$ by $\|v_1\|$,
How to recover $v_2$ from $\{o_2, o_1\}$

$$o_2 = \frac{v_2 - \langle v_2, o_1 \rangle o_1}{\|v_2\|}$$

$$v_2 = o_2 \|v_2\| + \langle v_2, o_1 \rangle o_1$$

$$o_3 = \frac{v_3 - \langle v_3, o_1 \rangle o_1 - \langle v_3, o_2 \rangle o_2}{\|v_3\|}$$

$$v_3 = o_3 \|v_3\| + \langle v_3, o_1 \rangle o_1 + \langle v_3, o_2 \rangle o_2$$

$v_2$ is defined by the second column of $R^{-1}$, in its first row, the pieces of $o_1$, we have to put $\langle v_2, o_1 \rangle$, in its second row we have to put $\|v_2\|$ the piece relative to $o_2$.

Each of these indicate how many pieces of $o_i$ are needed to built the respective $v_i$, because to build $v_i$, only is needed $o_j$ with $j \leq i$ that makes sense of why the matrix should be upper triangular.

The matrix $R^{-1}$ will be given by:

$$R^{-1}_{ii} = \|v_i\|$$
$$R^{-1}_{ji}, j < i, \langle v_i, o_j \rangle$$
