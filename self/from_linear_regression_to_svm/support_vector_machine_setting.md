$w \in R^n$,
$x \in R^n$,
$b \in R$

The points such that $wx = 0$, define a subspace of $R^n$ whose dimension is $(n-1)$ and those vectors are orthogonal with $w$.

**Question 1:** What's the distance of a point $x_0$, to that hyperplane:

It would be the length of the parallel vector to $w$, that passes through $x_0$, and intersects the plane, the distance of the vector defined the projection of $x_0$ on $w$, is precisely $(w \cdot x_0) / |w|$.

**Question 2:** if this set of points moves on the direction of $w$, how that is translated?

Each point $x$ is mapped to $\left( x + \frac{m \cdot w}{|w|} \right)$ and now:

$$
w \cdot \left( x + \frac{m \cdot w}{|w|} \right) = m \cdot |w|
$$

The distance of a vector $v$ to the hyperplane $wx = b$, is $| \langle w, v \rangle - b | / |w|$.

If $v_0$ is the projection of $v$ on this hyperplane then $\langle w, v_0 \rangle = b$, the detail is that:

$$
\begin{aligned}
\langle w, x \rangle &= b \\
\langle w, y + \frac{b w}{|w|^2} \rangle &= \langle w, y \rangle + b = b \\
&= \langle w, y \rangle = 0
\end{aligned}
$$