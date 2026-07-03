## Gram Schmidt

Let's say that the vectors of $M$ are $m_1, m_2, \dots, m_d$.

There is an algorithm or procedure to find a set of orthonormal vectors that span the same subspace by doing the following:

Set $q_1 = \frac{m_1}{\|m_1\|}$
    $q_2 = \frac{m_2 - \langle m_2, q_1 \rangle q_1}{\|m_2 - \langle m_2, q_1 \rangle q_1\|}$
    $q_3 = \frac{m_3 - \langle m_3, q_1 \rangle q_1 - \langle m_3, q_2 \rangle q_2}{\|m_3 - \langle m_3, q_1 \rangle q_1 - \langle m_3, q_2 \rangle q_2\|}$
    $\dots$

The idea is that once is known a set of orthonormal vectors, to add a new one: 

Take $m$, linear independent to the vectors on the set, subtract from $m$ its projection in the subspace formed by the orthonormal vectors, and normalize the resulting vector.

A fact here, if this new vector that is going to be added to the set, is a linear combination of the vectors in the set. That means it lies on the subspace those vectors span, which implies that its projection is the same vector, and thus the resulting vector is $0$, which breaks the algorithm. That's why the vectors have to be linearly independent.

$$
M = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix},\quad 
q_1 = \begin{pmatrix}1\\0\\0\end{pmatrix},\; q_2 = \begin{pmatrix}0\\1\\0\end{pmatrix},
$$
$$
m_3 - \langle m_3,q_1\rangle q_1 - \langle m_3,q_2\rangle q_2
= \begin{pmatrix}1\\1\\0\end{pmatrix} -1\begin{pmatrix}1\\0\\0\end{pmatrix} -1\begin{pmatrix}0\\1\\0\end{pmatrix}
= \begin{pmatrix}0\\0\\0\end{pmatrix}.
$$

After doing that, a matrix $Q$ $n \times d$ is obtained, i.e. $d$ vectors that are orthonormal. 

How to recover $m_1$ from $q_1$, multiply $q_1$ by $\|m_1\|$,
How to recover $m_2$ from $\{q_2, q_1\}$

$$\begin{align}
q_2 &= \frac{m_2 - \langle m_2, q_1 \rangle q_1}{\|m_2 - \langle m_2, q_1 \rangle q_1\|} \\
m_2 &= q_2 \|m_2 - \langle m_2, q_1 \rangle q_1\| + \langle m_2, q_1 \rangle q_1
\end{align}$$

$$\begin{align}
q_3 &= \frac{m_3 - \langle m_3, q_1 \rangle q_1 - \langle m_3, q_2 \rangle q_2}{\|m_3 - \langle m_3, q_1 \rangle q_1 - \langle m_3, q_2 \rangle q_2\|} \\
m_3 &= q_3 \|m_3 - \langle m_3, q_1 \rangle q_1 - \langle m_3, q_2 \rangle q_2\| + \langle m_3, q_1 \rangle q_1 + \langle m_3, q_2 \rangle q_2
\end{align}$$

See that those vectors $q_1, q_2, ...$ span the same subspace as the ones from $M$, because at every step the operation was:

$$q_i = m_i - (\text{linear combination of the previous vectors})$$

Those steps can be represented using linear transformations, starting from $M$ and ending at $Q$. 

Those linear transformations each is represented by a matrix upper triangular, since to build the next vector $q_i$ is only needed the current $v_i$ and the previous $q_i$ already obtained.

Set $M = M_0$. To obtain $q_1$ apply 

$$Z_1 = \begin{pmatrix}
\frac{1}{\|m_1\|} & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{pmatrix}$$

At the right of $M$, that's the first matrix. As a result $M_1 = MZ_1$ is obtained with $q_1$ on its first column. 

To obtain $q_2$ on the second column two steps are needed:

- Subtract $\langle q_1, v_2 \rangle$ from $v_2$, this is a linear transformation encoded by a matrix $Z_2$.
- Divide the resulting vector by $|v_2|$, that's other linear transformation $Z_3$.

After those two linear transformation a matrix $M_2$ will be obtained with $q_1$ on its first column, and $q_2$ on its second column. This process will be repeated until the matrix $Q$ is obtained.

The multiplication of all of those linear transformations is a matrix $Z$, so that $MZ = Q$. This matrix $Z$ contains on its diagonal entries the norms of the transformed vectors, which are nonzero because column vectors of $M$ are linearly independent. That's enough to ensure that $Z$ has an inverse, so $Z$ can be expressed as the inverse of a matrix $R$. 

$Z= R^{-1}$.

Finally $MZ = Q = MR^{-1}, M = QR$.