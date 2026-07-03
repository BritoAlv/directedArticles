## Projection in a Single Direction

Question: Let's say, in Euclidean space, $d$ dimensions. Fix a vector $v$, the projection of any vector $x$ on $v$ is a linear transformation, so what's its matrix?

$$v = m_1 e_1 + \dots + m_d e_d$$

$$Ax = \frac{\langle x, v \rangle}{\|v\|} v$$

$$\begin{align*}
A'x &= \langle x, v \rangle v \\
&= \langle x, v \rangle \\
&= v v^T x
\end{align*}$$

$$A = \frac{v v^T}{v^T v}$$

The matrix $v v^T$ has rank one as each column is a multiple of $v$.

This derivation is based on observing the algebraic values, but can't be interpreted easily, other way of deriving is by analyzing what $A$ does to the $e_i$ vectors, in fact, the columns of $A$, should be those values.

$$A(e_i) = v_i \cdot \frac{1}{\|v\|} v$$

This can be obtained by triangle similarity, $A$ is formed by the column vectors $v_i \cdot \frac{1}{\|v\|} v$, which makes clear the previous result, and the fact that the rank of the matrix is $1$, i.e. all of its columns are multiples of $v$.

Again, $A$ is a linear map whose columns indicate the effect of this linear map on the basis vectors $e_i$.

