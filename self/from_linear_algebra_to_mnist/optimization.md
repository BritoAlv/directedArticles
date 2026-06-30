## Maximizing Weighted Sum

There are $n$ positive coefficients, $c_1 \geq c_2 \geq \dots \geq c_n$. And $n$ positive variables $x_1, x_2, \dots, x_n$ each less than $1$ and they sum $d \leq n$. $d$ is an integer. What values should be assigned to the $x_i$ so that the weighted sum

$$
\sum_{i=1}^n c_i x_i
$$

is maximized?

Take any assignation of the values for the $x_i$, see that if $x_1$ could be increased and other $x_j$ decreased the sum will improve because $c_1 \geq c_j$, this forces that $x_1 = x_2 = \dots = x_d = 1$, others should be $0$.
