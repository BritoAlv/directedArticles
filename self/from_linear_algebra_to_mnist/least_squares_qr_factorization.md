## Least Squares.

In the least square problem the goal is finding the vector $x$ such that $\|v - Q R^{-1}x\|^2$ is minimized. 

$v$ is a $n * 1$ vector. $Q$ is an $n * d$ matrix whose columns $q_1, ..., q_d$ are orthonormal basis vectors. $QR^{-1} = M$.

 $M$ is $n* d$.

The projection of $v$ on each of the $q_i$ vectors is:

$\langle q_i, v \rangle = q_i^T v$

The coordinates of the projection of $v$ in the subspace formed by the $q$ vectors is:

$$
w = 
\begin{bmatrix}
\langle q_1, v \rangle \\
\langle q_2, v \rangle \\
\vdots \\
\langle q_d, v \rangle
\end{bmatrix} = Q^T v
\quad (  d \times 1)  
$$

The projection vector on that subspace is $\hat{v} = \sum_{i = 1}^d \langle q_i, v \rangle q_i$, or equivalently $Qw$.



From that we get that: 

$$ Qw = QR^{-1}x$$

Because $Q$ has orthonormal columns, then $Q^T Q = I$, multiply both sides by $Q^T$:

$$w = R^{-1} x$$

$$x = Rw$$

Finally, $x = RQ^Tv$.
