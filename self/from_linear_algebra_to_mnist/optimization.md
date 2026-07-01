## Maximizing Weighted Sum

There are $n$ positive coefficients, $c_1 \geq c_2 \geq \dots \geq c_n$. And $n$ positive variables $x_1, x_2, \dots, x_n$ each is at most $1$, and they sum $d \leq n$. $d$ is an integer. What values should be assigned to the $x_i$ so that the weighted sum:

$$
\sum_{i=1}^n c_i x_i
$$

Is maximized?

Take any assignation of the values for the $x_i$, see that if $x_1$ could be increased and other $x_j$ decreased by the same amount to keep their sum equal to $d$ the weighted sum will improve because $c_1 \geq c_j$. This forces that $x_1 = x_2 = \dots = x_d = 1$, others should be $0$.