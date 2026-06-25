# Principal Component Analysis

## Problem It Solves:

There is a list of vectors $S = \{v_1, v_2, \dots, v_N\}$ of an $n$-dimensional space $A$. The question is find a pair of matrices $M = d \times n$, $M' = n \times d$, that minimizes the following sum:

$$\sum_{v \in S} \|v - M' M v\|^2$$

Here is the catch, because $n > d$, it is not possible to obtain $(M' M v = v)$, so the question is find the pair of matrices $M'$, $M$ that minimize that sum.

See that the span of $M'Mv$ will be vectors of dimension at most $d$.

## How to Solve It:

Fix $M'$, from the least square problem is known that the quantity $\|v - M' (Mv)\|^2$ is minimized when $Mv$ is the vector such that $M'(Mv)$ is the projection of $v$ on the space spanned by $M'$.

This means that $M'$ fixes $M$, from the QR ideas is possible to find $Q'$ such that $M' = Q'R$ and $M$ should be $R^{-1}(Q')^T$, see that $M' M = Q' (Q')^T$, so its possible to use $Q'$ instead of $M$, and it has the plus that its columns are made of ortonormal vectors.

Let's assume that $M'$ is made up by ortonormal vectors, i.e, $d$ ortonormal vectors, $p_1, p_2, \dots, p_d$, then $Mv$ should be:

$$\sum_{i=1}^d \langle p_i, v \rangle p_i$$

Which happens when $M$ is precisely $(M')^T$ due to matrix multiplication.

Due to the projection, the vectors $v$, $M'(Mv)$, $(v - M'Mv)$ form a triangle that's rectangle.

$$\|v\|^2 = \|M'Mv\|^2 + \|(v - M'Mv)\|^2$$

Because the sum $\|v\|^2$ is fixed, minimizing the original sum is equivalent to maximize the sum of $\|M'Mv\|^2$, and at this point what can be done.

The idea is that because $M M' = I_d$, and $\|M'Mv\|^2 = \langle M'Mv, M'Mv \rangle$, get that:

$$\begin{align}
\|M'Mv\|^2 &= (M'Mv)^T \cdot (M' M v) \\
           &= (v^T M^T (M')^T)(M' M v) \\
           &= (v^T M' M) (M' M v) \\
           &= v^T M' M v
\end{align}$$

And what to do from here?

Using trace operator, it's possible to continue, using the fact that if $B$, $C$ are such that $BC$ and $CB$ are square matrices (so that $tr$ operator is defined), then $\text{tr}(BC) = \text{tr}(CB)$.

With this, taking $B = v^T M'$, $C = Mv$

$$\begin{align}
v   &= n \times 1 \\
v^T &= 1 \times n \\
M'  &= n \times d \\
M   &= d \times n
\end{align}$$

$$\begin{align}
B &= v^T M' = 1 \times d \\
C &= Mv = d \times 1
\end{align}$$

$$\begin{align}
BC &= 1 \times 1 \\
CB &= d \times d
\end{align}$$

$$\begin{align}
\|M'Mv\|^2 &= \text{tr}(v^T M' M v),\ \text{because it's a } 1 \times 1 \text{ matrix.} \\
           &= \text{tr}(Mv v^T M')
\end{align}$$

This expression is better because now it can be reduced to:

$$\text{tr}(M (v v^T) M')$$

Now this is a sum over all the $v$'s:

$$\sum_{v \in S} \text{tr}(M (v v^T) M')$$

Because matrix multiplication is distributive on the left and on the right, and $\text{tr}$ operator is additive, i.e., $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$, get that:

$$\sum_{v \in S} \text{tr}(M (v v^T) M') = \text{tr}(M (\sum_{v \in S} v v^T) M')$$

And at this point the problem becomes maximize the following:

$\text{tr}(M S M')$ where $S$ is the sum matrix $(n \times n)$.

$$\begin{align}
M &= d \times n \\
S &= n \times n \\
M' &= n \times d
\end{align}$$

$MSM'$ is a $d \times d$ matrix, from this point how to go on?

# What's an Example

# How Is Applied:

# How Is Computed:
