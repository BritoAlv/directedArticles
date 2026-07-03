# QR Factorization

## Why It Is Needed?

If there is a vector $v$ $n \times 1$, and a matrix $M$ $n \times d$.

The thing is the following, how find among of all the vectors of the form $Mw$, i.e. the span of $M$, the one $x$ that minimizes the following:

$$\|v - Mx\|^2$$

This vector $x$ has to be the projection of $v$ in the subspace determined by $M$. That's a result.

The thing is that this projection can't be found simply by doing the dot product between $v$ and every column vector of $M$ because the column vectors of $M$ don't have to be necessarily be orthonormal.

So what to do?

Find an orthonormal basis that spans the same subspace as $M$, find the projection in that space using that orthonormal basis, and then convert back to the coordinates of $M$. 

Applying Gram Schmidt is obtained $M = QR^{-1}$. The result is a matrix $R$ upper triangular, and a matrix $Q$ that spans the same subspace that $M$. With the additional property that the columns of $Q$ are made by orthonormal vectors.

The coefficients of the projection in the space spanned by $Q$ is $Q^T v$, the projection is $Q Q^T v$. 

Next step is take these coefficients to $M$ coordinates point of view. 

$R^{-1}$ contains the coefficients to go from $M$ point of view, to $Q$ point of view, because it's packing the coefficients needed to express the vectors of $M$ in terms of the ones in $Q$.

So if I have a vector in $M$, $Mx$, the vector is $Mx$ and $x$ are the coefficients of this vector in the $M$ basis. $Mx$ is how this vector looks like in the standard basis.

The coefficients to express each basis (column vectors of $M$) in terms of the basis of $Q$, are packaged in the matrix $R^{-1}$. 

The situation is reversed here, the coefficients in $Q^Tv$ are valid for $Q$ vectors point of view, to map it back to $M$ point of view, apply $R$ to it. $R$ is the matrix that contains the coefficients to express the $Q$ vectors in terms of the $M$ vectors. 

$RQ^T v$ will then contain the coefficients of the projection vector valid for the $M$ vectors. $x = RQ^Tv$

See that: 

$Mx = M (RQ^Tv) x = QR^{-1} R Q^T v = QQ^Tv = Q(Q^Tv)$

The projection vector of $v$ in the subspace in terms of $M$ have coefficients indicated by $x$, and in terms of $Q$ has coefficients $Q^Tv$.