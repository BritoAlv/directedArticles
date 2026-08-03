# Support Vector Machine

Given pairs of the form $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$, where $x_i$ are on $R^d$, and $y_i$ are points on $\{-1, 1\}$, the goal is to find a function $F$:

1. $F : R^d \to R$,
2. $F(x) = w^T x + b$, that means that $w$, $b$ have to be estimated.
3. Different from linear regression the condition here is that:
   $y_i \cdot (w^T x - b) > 0$ for all $i = 1, \ldots, m$

On a new vector the label output will be determined by the sign of $(w^T x - b)$

The set of points that separate the data in two classes are the ones where $w^T x = b$.

To separate correctly the data, there should exist solutions to the previous equation: $w^T x = b$, if there are too many, what makes one better than the other.

The criterion used here is computing for all the points its distance to the hyperplane defined by $\{x : w^T x = b\}$, take that minimal value among all of them, the goal is maximizing this minimal value, call it $M$.

The condition becomes:

$$
\max_{w, b} \left( \min_{x} \frac{w^T x - b}{|w|} \right)
$$

For any vector $w$ the scalar projection of $x$ onto the direction of $w$ is:

$$
\begin{aligned}
\operatorname{proj}_w(x) &= \left( \frac{\langle w, x \rangle}{|w|} \right) \cdot w \\
                         &= \left( \frac{w^T x}{|w|} \right) \cdot w
\end{aligned}
$$

It is the foot of the perpendicular line dropped from $x$ onto the line through the origin in direction $w$.

The distance of $x$ to the hyperplane is a segment parallel to the direction of $w$ that passed through $x$.

The hyperplane is not at the origin is shifted by $b$ units of distance, i.e. $b / |w|$.

That's the reason that the number $\left( \frac{w^T x - b}{|w|} \right)$ is the signed length of $x$ to the hyperplane defined by $(w, b)$.

Something that happens here is that the thing being maximized is scale invariant, this means that if I multiply by a constant $c$ both $w$, $b$ the result is:

$$
\begin{aligned}
\max_{w, b} \left( \min_{x} \frac{c w^T x - c b}{|c w|} \right) &= \max_{w, b} \left( \min_{x} \frac{w^T x - b}{|w|} \right)
\end{aligned}
$$

Let's say that $(w, b)$, $(w', b')$ represent the same hyperplane, are they up to a scaling factor?

See that the reverse direction is true:

$$
(w^T x = b) \Rightarrow c w^T x = c b
$$

The set of vectors such that $w^T x = b$, is a $(n-1)$-dimensional subspace, whose complement are the vectors such that $w^T x = 0$.

That's a 1 dimensional subspace, but if $w'^T$ spans represents this same subspace, then they should be one scalar version of the other.

After this, the scaling factor of $b'$ should be the same in $w'^T$ relative to $w$.

See that because the hyperplane is determined by $w = (\text{direction}, \text{a length})$, and a $b = (\text{shift})$, the thing being maximized is not changed by scaling.

$$
\begin{aligned}
= \max_{w, b} \frac{1}{|w|} \left( \min_{x} (w^T - b) \right)
\end{aligned}
$$

Can be assumed that $\min_{x} (w^T - b) = 1$, and the problem becomes minimize $|w|$, as the inverse problem of maximizing $1 / |w|$.

Minimize over $w$, $b$ $|w|$, s.t. $y_i (w^T x_i - b) \ge 1$.

See this optimization problem can be seen as a quadratic one:

$\min |w|$ is the same as $\min |w|^2$, and $|w|^2 = w^T w =$ sum of the squares of $w$ coordinates.

The inequalities are linear on those $w$ coordinates and $b$.

From this point, what one have here is an optimization problem.

The optimization problem has $n + 1$ constraints.