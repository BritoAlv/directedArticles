## Projection Matrix

Question: Let's say, in euclidean space, $d$ dimensions. Fix a vector $v$, the projection of any vector $x$ on $v$ is a linear transformation, so what's its matrix?

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

Again, $A$ is a linear map whose columns indicates the effect of this linear map on the basis vectors $e_i$.

That can be generalized, the general question, given a set of vectors $v_1, v_2, ..., v_d$ as columns of a matrix M, what's the matrix that indicates the linear transformation of a vector $v$ to its projection on the space spanned by $M$?

That matrix is called the pseudo-inverse of $M$.


## Scaling in a Specific Direction

### Standard Base

Now fix a vector $v$, for every vector $x$ there is another vector $\text{proj}_v x$ which is the projection of $x$ on $v$.

Question: Given a scalar factor $k$, what's the vector $y$ such that its projection on $v$ is $k$ times the projection on $v$ of $x$.

$$\begin{align*}
x &\mapsto \text{proj}_v x \\
y &\mapsto k \cdot \text{proj}_v x
\end{align*}$$

Observe that this question does not make sense, there are infinitely vectors $y$ such that their projection on $v$ is the vector $k \cdot (\text{proj}_v x)$, precisely because the projection map has rank $1 < \text{(number of dimensions of the space)}$.

To fix the question, let's choose $v = e_1$:

$$\begin{align*}
x &= x_1 e_1 + \dots x_d e_d \\
y &= k x_1 e_1 + \dots + x_d e_d
\end{align*}$$

Is the map that scales the first coordinate of every vector $x$, by a factor $k$, linear?

Its linear, so the next question is what is the matrix that describes this map?

Its matrix is $D = [e_1 \cdot k, e_2, e_3, \dots, e_d]$.

That was easy to do because the $e_i$ is the standard base, what if not?

## Custom Base

Question: Let's say there is a base $\{v_1, v_2, \dots, v_d\}$, and a vector $x$, what's the matrix of the linear transformation that scales $x$ by a factor of $k$ in the $v_1$ direction?

That means that:

$$\begin{align*}
T(v_1) &= k \cdot v_1 \\
T(v_i) &= v_i, \ i \geq 2
\end{align*}$$

One intuitive approach is write:

$$\begin{align*}
A(e_i) &= v_i \\
B(v_i) &= e_i, B = A^{-1} \\
D &= [e_1 \cdot k, e_2, e_3, \dots, e_d].
\end{align*}$$

The matrix needed is:

$$ADA^{-1}$$

Take the vectors from the standard base, to the $v$ base, apply the scaling there, since it's easy to do, and then take them back to the standard base.

There is other approach which is the following:

Let $P$ be the linear map that:

$$\begin{align*}
P(v_1) &= v_1 \\
P(v_i) &= 0, \ i \geq 2
\end{align*}$$

In essence gives the $v_1$ part of a vector. Here a detail is that to define this linear map a base which includes $v_1$ is needed. To define a linear map is needed to specify what it does to all the vectors of a base.

Let $T$ be the matrix that does the job:

$$\begin{align*}
x &= Px + (x - Px) \\
Tx &= k \cdot Px + (x - Px) \quad \text{(2)} \\
Tx &= (k \cdot P + I - P)x
\end{align*}$$

From this the matrix $T$ should be equal to $(k \cdot P + I - P) = (P \cdot (k - 1) + I)$.

The second step was justified because $T$ does nothing to the $(x - Px)$ part of $x$.

## Making Sense of the Two Approaches.

The next question is understand why $(P \cdot (k - 1) + I)$ represent the same linear transformation that $ADA^{-1}$ represents.

Again still is the question of why algebraically it should be the case that:

$ADA^{-1}$ is equal to $(P \cdot (k - 1) + I)$

$(P * (k-1) + I)x$

See that:

$$D = I + (k-1) \cdot E$$

$E$ is a matrix that has a $1$ on the $(1, 1)$ coordinate, and $0$ everywhere else.

See that $E$ is the projection linear map on $e_1$, relative to the standard base $e$.

$$\begin{align*}
& A ( I + (k-1) \cdot E ) A^{-1} x \\
& A ( I + (k-1) \cdot E ) A^{-1} \\
&= A I A^{-1} + A \cdot [(k-1) \cdot E] A^{-1} \\
&= I + (k-1) \cdot A E A^{-1}
\end{align*}$$

Remains to prove that $AEA^{-1} = P$.

But this is linear transformations issue, change of basis issue. Here it goes.

When starting with $x$, two interpretations:

1. if $x$ is a vector on the $v$-basis, then $A^{-1}x$ is how its twin in the $e$-basis, looks like in the $v$-basis.
2. if $x$ is a vector on the $e$-basis then $A^{-1}x$ is how this vector looks like in the $v$-basis.
3. if $y$ is a vector on the $v$-basis, then $Ay$ is how this vector looks like in the $e$-basis.
4. if $y$ is a vector on the $e$-basis, then $Ay$ is how its twin in the $v$-basis looks like in the $e$-basis.

So using all of this: start with a vector $x = [x_1, x_2, \dots, x_d]$ on the $e$-basis.

By $(2)$, $(A^{-1}x)$ is how this vector looks like in the $v$-basis $[c_1, c_2, \dots, c_d]$,

The effect of $E$ is that take only its first coordinate, $\rightarrow [c_1, 0, 0, \dots, 0]$ and then by $(3)$ $A (E (A^{-1} x))$ is how this vector looks like in the $e$-basis. See that $E \cdot A^{-1}x$ is of the form $[c_1, \ 0, \ 0, \ 0, \dots,  0]$, so $A \cdot (E \cdot A^{-1}x)$ is $v_1 \cdot c_1$. That's what $P$ does.

## Multiple Scaling

Now what if is needed to scale by $k_1$ in the direction of $v_1$, and by $k_2$ in the direction of $v_2$. From the previous analysis:

Way $1$: $A_1 = AD_1 A^{-1}$, $A_2 = AD_2 A^{-1}$

Way $2$: $A_1 = (k_1-1)P_1 + I$, $A_2 = (k_2-1)P_2 + I$

Question 1:

By the previous conclusions, the linear map, or matrix of each of those transformations, can be obtained, individually.

The thing is why makes sense that multiplying them is the result of applying the two operations, one after the other.

Also see that it should be commutative because the order on which scaling is made, does not affect the other.

This is because scaling in one direction, don't change the others.

This way it's easy to see that the multiplication does the job, because:

$$\begin{align*}
(A_1 A_2) &= AD_1 A^{-1} \cdot AD_2 A^{-1} \\
&= A D_1 D_2 A^{-1}
\end{align*}$$

See that's precisely the effect and $D_1 D_2 = D_2 D_1$, they are diagonal matrices.

$$\begin{align*}
D_1 &= I + (k_1 - 1)E_{11} \\
D_2 &= I + (k_2 - 1)E_{22} \\
D_1 D_2 &= I + (k_1 - 1)E_{11} + (k_2 - 1)E_{22}
\end{align*}$$

$$\begin{align*}
& A D_1 D_2 A^{-1} \\
&= A (I + (k_1 - 1)E_{11} + (k_2 - 1)E_{22}) A^{-1} \\
&= I + (k_1-1)A E_{11} A^{-1} + (k_2-1)A E_{22} A^{-1}
\end{align*}$$

The other way,

$$\begin{align*}
& ((k_1 - 1)P_1 + I) \cdot ((k_2 - 1)P_2 + I) \\
&= (k_1 - 1)(k_2 - 1)P_1P_2 + I + (k_1-1)P_1 + (k_2-1)P_2,
\end{align*}$$

Because projecting in $P_2$, and then on $P_1$, is $0$, $P_2$ zeroes the coordinate that $P_1$ extracts later. End up with:

$$= I + (k_1 - 1)P_1 + (k_2 - 1)P_2$$

And by the previous analysis, $(k_1 - 1)A E_{11} A^{-1}$ is $P_1$, so it all makes sense algebraically.

## Projection Matrix, Versus Projection on Base.

See that, the linear map that scales $v_1$ by $k$, and leaves untouched the other vectors on that base, does not necessarily has to be the projection linear map on $v_1$, because it depends on the other vectors of the basis.

That could be the projection linear transformation or not, to see why use other basis different than $v$ that still contains $v_1$, the linear transformation will be different, because it depends on the basis.

The orthogonal projection on $v_1$ is only one.

So what is needed to ensure on $\{v_1, v_2, \dots, v_d\}$ that the linear transformation $P$ matches with the orthogonal projection on $v_1$.

$$\begin{align*}
P' &= \text{projection linear transformation} \\
P &= \text{projection using } v_i \text{ basis.}
\end{align*}$$

See the differences:

$i = 1$:

$$\begin{align*}
P'(v_1) &= v_1 \\
P(v_1) &= v_1
\end{align*}$$

$i \geq 2$:

$$\begin{align*}
P'(v_i) &= \frac{\langle v_1, v_i \rangle}{\langle v_1, v_1 \rangle} v_1 \\
P(v_i) &= 0
\end{align*}$$

For them to match it should be that $\langle v_1, v_i \rangle = 0$, which means that all of those vectors $v_i$ should be orthogonal to $v_1$.

Basically $P'$ decomposes the space into $\text{span}(v_1)$ and its orthogonal complement which is a space whose basis vectors are all orthogonal to $v_1$.

The thing is that $P$ here is the operator such that:

$$\begin{align*}
P(v_1) &= v_1 \\
P(v_j) &= 0 \text{ for } j \geq 2
\end{align*}$$

Which does not have to match with the operator that does the projection of any vector on $v_1$, that operator is defined by:

$$P'(v_i) = \frac{\langle v_i, v_1 \rangle}{\|v_1\|^2} v_1$$

Again for them to match it should be the case that $\langle v_i, v_1 \rangle = 0$, if $i \neq 1$.