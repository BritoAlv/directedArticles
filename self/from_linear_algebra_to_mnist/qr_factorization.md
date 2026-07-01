# QR Factorization

## Why It Is Needed?

If there is a vector $v$ $n \times 1$, and a matrix $M$ $n \times d$.

The thing is the following, how find among of all the vectors of the form $Mw$, i.e. the span of $M$, the one $x$ that minimizes the following:

$$\|v - Mx\|^2$$

This vector $x$ have to be the projection of $v$ in the subspace determined by $M$. That's a result.

The thing is that this projection can't be found simply by doing the dot product between $v$ and every column vector of $M$ because the column vectors of $M$ don't have to be necessarily be orthonormal.

So what to do?

Find an orthonormal basis that spans the same subspace as $M$, find the projection in that space using that orthonormal basis, and then convert back to the coordinates of $M$. 

Applying Gram Schmidt is obtained $M = QR^{-1}$. The result is a matrix $R$ upper triangular, and a matrix $Q$ that spans the same subspace that $M$. With the additional property that the columns of $Q$ are made by orthonormal vectors.

Next, given $R^{-1}$:

$$M R R^{-1} = Q R^{-1}$$
$$M = Q R^{-1}$$

$Q$ is a matrix formed by $d$ column vectors orthonormals, and $R^{-1}$ is an upper triangular matrix.


