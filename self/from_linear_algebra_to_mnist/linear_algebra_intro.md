# Linear Algebra Related to Diagonalization:

## What Means $A\mathbf{x}$?

Starting with a $d \times d$ square matrix $A$, made of column vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_d$, and a vector $\mathbf{x}$:

$A$ is made by the column vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_d$, so this means that:

$$A(\mathbf{e}_i) = \mathbf{v}_i$$

So $A$ is a linear map that maps each of the standard basis vectors to other vectors $\mathbf{v}_i$ respectively. $A$ is the unique linear map that sends each basis vector $\mathbf{e}_j$ to $\mathbf{v}_j$.

From this definition if $\mathbf{x} = \begin{bmatrix} a \\ b \\ c \end{bmatrix}$, then $A\mathbf{x}$ is the vector in standard basis whose coordinates in the $\mathbf{v}$-basis are precisely $\begin{bmatrix} a \\ b \\ c \end{bmatrix}$.

$$A\mathbf{x} = x_1 \mathbf{v}_1 + \dots + x_d \mathbf{v}_d$$
$$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

$$\mathbf{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$
$$\mathbf{v}_2 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$
$$\mathbf{x} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}_V = A\mathbf{x} = \begin{bmatrix} 10 \\ 11 \end{bmatrix}_{\text{standard}}.$$

$$\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_d \rightarrow A(\mathbf{e}_1) = \mathbf{v}_1, A(\mathbf{e}_2) = \mathbf{v}_2, \dots, A(\mathbf{e}_d) = \mathbf{v}_d$$

$$\begin{align*}
A(\mathbf{x}) &= A(x_1 \mathbf{e}_1 + x_2 \mathbf{e}_2 + \dots + x_d \mathbf{e}_d) \\
              &= x_1 A(\mathbf{e}_1) + x_2 A(\mathbf{e}_2) + \dots + x_d A(\mathbf{e}_d) \\
              &= x_1 \mathbf{v}_1 + \dots + x_d \mathbf{v}_d \\
              &= 3 \cdot \begin{bmatrix} 2 \\ 1 \end{bmatrix} + 4 \cdot \begin{bmatrix} 1 \\ 2 \end{bmatrix} \\
              &= \begin{bmatrix} 10 \\ 11 \end{bmatrix}
\end{align*}$$

The final result $\begin{bmatrix} 10 \\ 11 \end{bmatrix}$ is the same vector but the interpretation on what's $\mathbf{x}$ is different. In the sense that $\begin{bmatrix} 3 \\ 4 \end{bmatrix}_{\text{standard}} \neq \begin{bmatrix} 3 \\ 4 \end{bmatrix}_{\mathbf{v}_i}$.

From that is clear that if there is a vector on the $\mathbf{v}$ basis and is needed to see how it looks in the standard base $\mathbf{e}$ what has to be done is apply $A$ to it.

See that it doesn't tell how a vector in the standard basis looks like in the $\mathbf{v}$-basis.

If $\mathbf{x}$ is interpreted as a vector on the standard basis, what $A\mathbf{x}$ returns is a vector on the standard basis. The only relation that it has with $\mathbf{x}$ is that it is mapped version.

The effect of $A\mathbf{x}$ on $\mathbf{x}$ is the following. If $\mathbf{x}$ is seen as a coordinate vector on the basis formed by the columns of $A$, thus $A\mathbf{x}$ is writing that vector on the standard base coordinate. 

It is mapping coordinates from the base $A$ to the standard base. And why to the standard base, $\mathbf{e}_i$, because the column vectors of $A$: $v$ are written in terms of this base $\mathbf{e}$.

## Inverse Of $A$?

See that if $\mathbf{x}$ on the $\mathbf{v}$ basis is $(3, 4)$ then is known that on the standard basis it's $(10 \ 11)$, but if $\mathbf{x}$ is on the standard basis $(3, 4)$ then how it looks on the $\mathbf{v}$-basis. 

That's the next question.

The natural idea is to build a linear transformation $B$ that does the opposite of $A$, i.e. $B(\mathbf{v}_i) = \mathbf{e}_i$.

The interpretation from before was that $A(\mathbf{e}_i) = \mathbf{v}_i$, vectors $\mathbf{v}$ written in the $\mathbf{e}_i$ base, will be mapped to the vector on the $\mathbf{e}_i$ that looks like $\mathbf{v}$ in the $\mathbf{v}_i$ base.

$$\mathbf{x} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}_{\text{std}} \rightarrow \begin{bmatrix} 10 \\ 11 \end{bmatrix}_{\text{std}} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}_{\mathbf{v}_i}$$

Replacing the same interpretation: $B(\mathbf{v}_i) = \mathbf{e}_i$, vectors $\mathbf{v}$ written in the $\mathbf{v}_i$ base, will be mapped to the vector on the base $\mathbf{v}_i$ that looks like $\mathbf{v}$ in the $\mathbf{e}_i$ base.

$$\mathbf{x} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}_{\text{std}}$$
$$\mathbf{x} = \begin{bmatrix} a \\ b \end{bmatrix}_{\mathbf{v}_i} \rightarrow B\mathbf{x}_{\mathbf{v}_i} = \begin{bmatrix} a \\ b \end{bmatrix}_{\mathbf{e}_i}$$

That means that if is known the representation of a vector in the $\mathbf{v}_i$ basis, then applying $B$ to it, will give the representation of it in the $\mathbf{e}_i$ basis.

Is not known what $B$ does to the basis vectors, i.e., $B(\mathbf{e}_i) = ?$

Let's say that $B(\mathbf{e}_i) = \mathbf{r}_i$, then $B = [\mathbf{r}_1 \ \mathbf{r}_2 \ \dots \ \mathbf{r}_d]$, $R = \{\mathbf{r}_1, \mathbf{r}_2, \dots, \mathbf{r}_d\}$ is another basis.

Can I compute $\mathbf{r}_i$ in terms of the base $\mathbf{v}$?

$$\begin{align*}
      B (\mathbf{e}_i) &= B (c_1 \mathbf{v}_1 + \dots + c_d \mathbf{v}_d) \\
      &= c_1 \cdot \mathbf{e}_1 + \dots + c_n \mathbf{e}_n
\end{align*}$$

Those $c_i$ coefficients are from trying to express $e_i$ in the base $\mathbf{v}$. This makes sense: 

From the previous interpretation is known that:

$$ A = [\mathbf{v}_1 \ \mathbf{v}_2 \ \dots \ \mathbf{v}_d]$$

See, those vectors are defined in terms of $\mathbf{e}_i$, if a vector, represented in the $\mathbf{v}_i$ base, is multiplied by this matrix, the result is how it looks in the $\mathbf{e}_i$ base. 

If there is a matrix $B = [\mathbf{r}_1 \ \mathbf{r}_2 \ \dots \ \mathbf{r}_d]$ where $\mathbf{r}_1 \ \mathbf{r}_2 \ \dots \ \mathbf{r}_d$ are defined by expressing the base $\mathbf{e}$ in terms of $\mathbf{v}$, multiply a vector represented in the $\mathbf{e}_i$ base, by this matrix, the result is how it looks in the $\mathbf{v}_i$ base. Same idea, but with different bases.

Keeping this in mind, I can try to build the intuition here, see the reason that diagonalization is like $M D M^{-1}$.

$M^{-1} \mathbf{x}$ maps $\mathbf{x}$ from standard coordinates to eigen-vectors coordinates, and then $M$ takes it back to standard coordinates. $D$ only do scaling on the vectors expressed on the eigen-vectors base.

## $A = BC$

What conclusions can be obtained from a relationship like $A = BC$?

$Ax$ is a vector in standard coordinates whose coefficients in the $A$ coordinates are given by $x$, $C$ is packaging how express $A$ column vectors in terms of $B$ vectors. 

Equivalently column vectors of $A$ can be written as linear combination of vectors on $B$, and the coefficients are packaged on $C$. 

The span of $A$ is a subset of the span of $B$, and to be the same the condition is that $C$ can be inverted. That would be the matrix that packages the inverse process, writing the column vectors of $B$ in terms of the column vectors of $A$. 

See that $B(Cx)$, $Cx$ are the coefficients of the vector $B(Cx) = Ax$ on the $B$ basis. There are two representations of the common vector $v = Ax = B(Cx)$, using the column vectors of $A$, and other using the column vectors of $B$. 