## Proof That the Perceptron Algorithm Converges

This proof is assuming the optimal vector don't have its norm constrained.

Let $w^*$ be the optimal vector, this is the one that maximizes the margin.

$$
|w^*| = B
$$

Assuming it exists:

The algorithm starts with $w^1 = 0$, every time it founds a bad labeled sample $x_i$ with $y_i w^t x_i < 0$, an update is made:

$$
w^{t+1} = w^t + y_i x_i
$$

Observe that:

$$
\begin{aligned}
\langle w^*, w^{t+1} \rangle - \langle w^*, w^t \rangle
&= \langle w^*, y_i x_i \rangle \\
&= y_i \langle w^*, x_i \rangle \ge 1
\end{aligned}
$$

The conclusion is that $\langle w^*, w^{t+1} \rangle \ge t$

$$
\begin{aligned}
|w^{t+1}|^2 &= |w^t + y_i x_i|^2 \\
            &= |w^t|^2 + 2 y_i \langle w^t, x_i \rangle + y_i^2 |x_i|^2 \\
            &\le |w^t|^2 + 2 y_i \langle w^t, x_i \rangle + R^2 \\
            &\le \sqrt{|w^t|^2 + R}
\end{aligned}
$$

$y_i \langle w^t, x_i \rangle < 0$, holds because $x_i$ is misclassified.

So $|w^{t+1}| \le \sqrt{t}R$

$$
\begin{aligned}
\langle w^*, w^{t+1} \rangle &\ge \frac{t}{|w^*| |w^{t+1}|} \\
                              &\ge \frac{\sqrt{t}}{RB}
\end{aligned}
$$

$$
\begin{aligned}
1 &\ge \frac{\sqrt{t}}{RB} \\
t &\le (RB)^2
\end{aligned}
$$

$B$ is the length of the optimal vector.

$R$ is the maximal length among the lengths of the $x_i$ vectors.
