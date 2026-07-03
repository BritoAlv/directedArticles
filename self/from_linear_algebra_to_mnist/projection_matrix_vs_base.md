## Projection Matrix, Versus Projection on Base.

See that, the linear map that scales $v_1$ by $k$, and leaves untouched the other vectors on that base, does not necessarily has to be the projection linear map on $v_1$, because it depends on the other vectors of the basis.

That could be the projection linear transformation or not. To see why, use other basis different of $v$ that still contains $v_1$, the linear transformation will be different, because it depends on the other vector of the basis.

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

Which does not has to match with the operator that does the projection of any vector on $v_1$, that operator is defined by:

$$P'(v_i) = \frac{\langle v_i, v_1 \rangle}{\|v_1\|^2} v_1$$

Again for them to match it should be the case that $\langle v_i, v_1 \rangle = 0$, if $i \neq 1$.