## Column Transformations on the Right

Given a matrix $M$ with column vectors $m_1, m_2, ..., m_d$, subtracting $k$ times $m_i$ from $m_j$ can be represented with the following matrix $P$:

$$
P = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & -k \\
0 & 0 & 1
\end{pmatrix}
\qquad (\text{example for } i=2,\; j=3,\; k=2)
$$

The $j$ column of $P$ indicate the pieces of each $m_i$ that will be used to transform it into a new vector, thus put $1$ on the $j$ row and $-k$ in the $i$ row.

Fix a column let's say $i$, it is made by $p_{i1}, p_{i2}, \dots, p_{id}$, see that each of those coefficients $p_{ij}$, determines how much the vector $m_j$ will contribute to the transformed version of $m_i$. It's like take $m_i$ will be mapped to a vector formed by $p_{ij}$ pieces of the vector $m_j$.

$$
\text{Example: } i=3,\; j=3,\; P_{\bullet 3} = \begin{pmatrix}0 \\ -k \\ 1\end{pmatrix}
\quad\Rightarrow\quad m_3' = 0\cdot m_1 + (-k)\cdot m_2 + 1\cdot m_3 = m_3 - k\,m_2.
$$

The result will be a new matrix $MP$.

$$
M = \begin{pmatrix} | & | & | \\ m_1 & m_2 & m_3 \\ | & | & | \end{pmatrix}, \qquad
MP = \begin{pmatrix} | & | & | \\ m_1 & m_2 & m_3 - k\,m_2 \\ | & | & | \end{pmatrix}
$$

Scaling by $k$ the $i$ basis vector is encoded with the matrix:

$$I + (k - 1)e_i e_i^T$$

$$
\text{For } i=2,\; k=3:\quad I + 2 e_2 e_2^T = \begin{pmatrix}
1 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

Observe that column vectors of $MP$ are described by coefficients of $P$ as linear combinations of the column vectors of $M$.