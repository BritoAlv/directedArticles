## Projection Matrix

Question: Let's say, in euclidean space, $d$ coordinates, fix a vector $v$, the projection of any vector $x$ on $v$ is a linear transformation, so what's its matrix?

$v = m_1 e_1 + \dots + m_d e_d$

$Ax = \frac{\langle x, v \rangle}{\|v\|} v$

$A'x = \langle x, v \rangle v$
    $= \langle x, v \rangle$
    $= v v^T x$

$A = \frac{v v^T}{v^T v}$

Observe that the matrix $v v^T$ has rank one as each column is a multiple of $v$.

This derivation is based on observing the algebraic values, but can't be interpreted easily, other way of deriving is by analyzing what $A$ does to the $e_i$ vectors, in fact, the columns of $A$, should be those values.

$A(e_i) = v_i \cdot \frac{1}{\|v\|} v$

This can be obtained by triangle similarity, finally $A$ is formed by the column vectors $v_i \cdot \frac{1}{\|v\|} v$, which makes clear the previous result, and the fact that the rank of the matrix is $1$. ie all of its columns are multiples of $v$.

Again, the columns of a matrix $A$ that indicates a linear map are the effect of this linear map on the basis vectors $e_i$.

## Scaling in a Specific Direction

Now fix a vector $v$, for every vector $x$ there is another vector $\text{proj}_v x$ which is the projection of $x$ on $v$, question, given a scalar factor $k$:

What's the vector $y$ such that:

$x \mapsto \text{proj}_v x$
$y \mapsto k \cdot \text{proj}_v x$

Observe that this question does not make sense, there are infinitely vectors $y$ such that their projection on $v$ is the vector $k \cdot (\text{proj}_v x)$, precisely because the projection map has rank $1 < \text{(number of dimensions of the space)}$.

To fix the question, let's assume that:

$x = x_1 e_1 + \dots x_d e_d$

$y = k x_1 e_1 + \dots + x_d e_d$

Is the map that scales the first coordinate of every vector $x$, by a factor $k$, linear?

Its linear, so the next question is what is the matrix that describes this map?

Its matrix is $D = [e_1 \cdot k, e_2, e_3, \dots, e_d]$.

That was easy to do because the $e_i$ is the standard base, what if not?

Question, let's say there is a base $\{v_1, v_2, \dots, v_d\}$, and a vector $x$, what's the matrix of the linear transformation that scales $x$ by a factor of $k$ in the $v_1$ direction?

One intuitive approach is write:

$A(e_i) = v_i$

$B(v_i) = e_i, B = A^{-1}$

The matrix we are looking for is: $ADA^{-1}$, take the vectors from the standard base, to the $v$ base, apply the scaling there, since it's easy to do, and then take them back to the standard base.

There is other approach which is the following:

Let $P$ be the projection matrix on the vector $v_1$, and $T$ the matrix we are looking for:

$x = Px + (x - Px)$

$Tx = k \cdot Px + (x - Px)$
$Tx = (k \cdot P + I - P)x$

From this we get that the matrix $T$ should be equal to $(k \cdot P + I - P) = (P \cdot (k - 1) + I)$.

The next question is understand why $(P \cdot (k - 1) + I)$ represent the same linear transformation that $ADA^{-1}$ represents.

There is a problem in the previous approach, what's being done is scale the $v_1$ component in a basis that $v_1$ is part of.

That could be the projection linear transformation or not, to see why use other basis different than $v$ that still contains $v_1$, the linear transformation will be different, because it depends on the basis.

The projection linear transformation is only one,

So what is needed to ensure on $\{v_1, v_2, \dots, v_d\}$ so the linear transformation we are describing matches with the projection linear transformation.

$P = \text{projection linear transformation}$

$T = \text{projection using } v_i \text{ basis.}$

The projection linear transformation what does is:

$P(v_1) = v_1$

$T(v_1) = v_1$

$P(v_i) = \frac{\langle v_1, v_i \rangle}{\langle v_1, v_1 \rangle} v_1$

$T(v_i) = 0$

For them to match we should have that $\langle v_1, v_i \rangle = 0$, which means that all of those vectors $v_i$ should be orthogonal to $v_1$.

Basically $P$ decomposes the space into $\text{span}(v_1)$ and its orthogonal complement which is a space whose basis vectors are all orthogonal to $v_1$.

Again still is the question of why algebraically it should be the case that:

$ADA^{-1}$ is equal to $(P \cdot (k - 1) + I)$

$D = I + (k-1) \cdot E$

$E$ is a matrix that has a $1$ on the $(1, 1)$ coordinate, and $0$ everywhere else. 

See that $E$ is the projection linear map on $e_1$, relative to the standard base $e$.

$A ( I + (k-1) \cdot E ) A^{-1} x$

$A ( I + (k-1) \cdot E ) A^{-1}$

$= A I A^{-1} + A \cdot [(k-1) \cdot E] A^{-1}$

$= I + (k-1) \cdot A E A^{-1}$

Remains to prove that $AEA^{-1} = P$.

But this is linear transformations issue, change of basis issue. Here it goes.

When starting with $x$, two interpretations:

 1. if $x$ is a vector on the $v$-basis, then $A^{-1}x$ is how its twin in the $e$-basis, looks like in the $v$-basis.
 2. if $x$ is a vector on the $e$-basis then $A^{-1}x$ is how this vector looks like in the $v$-basis.
 3. if $y$ is a vector on the $v$-basis, then $Ay$ is how this vector looks like in the $e$-basis.
 4. if $y$ is a vector on the $e$-basis, then $Ay$ is how its twin in the $v$-basis looks like in the $e$-basis.

So using all of this, we start with a vector $x = [x_1, x_2, \dots, x_d]$ on the $e$-basis.

By (2), we get that $(A^{-1}x)$ is how this vector looks like in the $v$-basis $[c_1, c_2, \dots, c_d]$,

The effect of $E$ is that take only its first coordinate, $\rightarrow [c_1, 0, 0, \dots, 0]$ and then by (3) $A (E (A^{-1} x))$ is how this vector looks like in the $e$-basis. See that $E \cdot A^{-1}x$ is of the form $[c_1 \ 0 \ 0 \ 0, \dots,  0]$, so $A \cdot (E \cdot A^{-1}x)$ is $v_1 \cdot c_1$, which is precisely what $P$ does to a vector on the standard base, so those two linear transformations are the same.

How in this proof was used the fact, that each vector $\{v_2, \dots, v_d\}$ has to be orthogonal to $v_1$.

The thing is that $P$ here is the operator such that:
    $P(v_1) = v_1$
    $P(v_j) = 0$ for $j \geq 2$

Which does not have to match with the operator that does the projection of any vector on $v_1$, that operator is defined by:

$$P(v_i) = \frac{\langle v_i, v_1 \rangle}{\|v_1\|} v_1$$

Again for them to match it should be the case that $\langle v_i, v_1 \rangle = 0$, if $i \neq j$.
