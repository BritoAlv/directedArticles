## Column Transformations on the Right

Given a matrix $M$ with column vectors $m_1, m_2, ..., m_d$, subtracting $k$ times $m_i$ from $m_j$ can be represented with the following matrix $P$:

The $j$ column of $P$ indicate the pieces of each $m_i$ that will be used to transform it into a new vector, thus put $1$ on the $j$ row and $-k$ in the $i$ row.

Fix a column let's say $i$, it is made by $p_{i1}, p_{i2}, \dots, p_{id}$, see that each of those coefficients $p_{ij}$, determines how much the vector $m_j$ will contribute to the transformed version of $m_i$. It's like take $m_i$ will be mapped to a vector formed by $p_{ij}$ pieces of the vector $m_j$.

The result will be a new matrix $MP$.

Scaling by $k$ the $i$ basis vector is encoded with the matrix:

$$I + (k - 1)e_i e_i^T$$