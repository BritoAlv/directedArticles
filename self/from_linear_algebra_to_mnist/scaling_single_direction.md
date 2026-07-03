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

One intuitive approach is writing:

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

The next question is why $(P \cdot (k - 1) + I)$ represent the same linear transformation that $ADA^{-1}$ represents.

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

1. If $x$ is a vector on the $v$-basis, then $A^{-1}x$ is how its twin in the $e$-basis, looks like in the $v$-basis.
2. If $x$ is a vector on the $e$-basis then $A^{-1}x$ is how this vector looks like in the $v$-basis.
3. If $y$ is a vector on the $v$-basis, then $Ay$ is how this vector looks like in the $e$-basis.
4. If $y$ is a vector on the $e$-basis, then $Ay$ is how its twin in the $v$-basis looks like in the $e$-basis.

So using all of this: start with a vector $x = [x_1, x_2, \dots, x_d]$ on the $e$-basis.

By $(2)$, $(A^{-1}x)$ is how this vector looks like in the $v$-basis $[c_1, c_2, \dots, c_d]$,

The effect of $E$ is that take only its first coordinate, $\rightarrow [c_1, 0, 0, \dots, 0]$ and then by $(3)$ $A (E (A^{-1} x))$ is how this vector looks like in the $e$-basis. See that $E \cdot A^{-1}x$ is of the form $[c_1, \ 0, \ 0, \ 0, \dots,  0]$, so $A \cdot (E \cdot A^{-1}x)$ is $v_1 \cdot c_1$. That's what $P$ does.