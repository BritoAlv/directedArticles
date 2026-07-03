## Finding the Projection Matrix in a Non-Orthogonal Basis

See that the least square problem is about a fixed subspace indicated by a matrix $M$, find the vector $x$, such that:

$$\|b - Mx\|^2$$

Is minimized. 

The solution is to find the vector $x$ such that $Mx$ is the projection of $b$ in that subspace.

$b$ is $n \times 1$, $M$ is $n \times d$, $M^T$ is $d \times n$, $x$ is $d \times 1$.

To solve that issue one necessary condition is check that $\langle b - Mx, Mx \rangle =0$, but this is not enough, since the projection vector should be orthogonal to all the vectors on the subspace spanned by $M$, not one of them, $Mx$ in this case. 

Let $m_1, m_2, ..., m_d$ the column vectors of $M$, the enough condition is that the $d$ equations, $\langle b - Mx, m_i \rangle =0$ are satisfied by some $x$.

Which can be written in matrix form as $(b - Mx)^T M = 0$, or equivalently $M^T (b - Mx) = 0$, from this is obtained that:

$$M^T b = M^T M x$$

1. $M$ is made by linearly independent column vectors, then:

$$
\begin{align}
M^T M x &= 0 \\
x^T M^T M x &= 0 \\
(Mx)^T (Mx) &= 0 \\
|Mx|^2 &= 0
\end{align}
$$

Because columns of $M$ are linearly independent the only solution to that equation is $x = 0$. The solution is $x = (M^T M)^{-1} M^T b$. 

2. If column vectors are linearly dependent, then there are many $x$ that satisfy the equation and so that $Mx$ is the projection of $b$ in the subspace spanned by $x$.

From the previous analysis, assuming linearly independent columns if $M = QR^{-1}$, then $x = RQ^Tb$, and from this analysis we get other expression for $x$ written only in terms of $M$.

It should be the case that:

$$(M^T M)^{-1} M^T = R Q^T$$
