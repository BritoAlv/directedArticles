## Multiple Scaling

Now what if is needed to scale by $k_1$ in the direction of $v_1$, and by $k_2$ in the direction of $v_2$. From the previous analysis:

Way $1$: $A_1 = AD_1 A^{-1}$, $A_2 = AD_2 A^{-1}$

Way $2$: $A_1 = (k_1-1)P_1 + I$, $A_2 = (k_2-1)P_2 + I$

Question 1:

By the previous conclusions, the linear map, or matrix of each of those transformations, can be obtained, individually.

The thing is why makes sense that multiplying them is the result of applying the two operations, one after the other.

Also see that it should be commutative because the order on which scaling is made, does not affect the other.

This is because scaling in one direction, don't change the others.

This way it's easy to see that the multiplication does the job, because:

$$\begin{align*}
(A_1 A_2) &= AD_1 A^{-1} \cdot AD_2 A^{-1} \\
&= A D_1 D_2 A^{-1}
\end{align*}$$

See that's precisely the effect and $D_1 D_2 = D_2 D_1$, they are diagonal matrices.

$$\begin{align*}
D_1 &= I + (k_1 - 1)E_{11} \\
D_2 &= I + (k_2 - 1)E_{22} \\
D_1 D_2 &= I + (k_1 - 1)E_{11} + (k_2 - 1)E_{22}
\end{align*}$$

$$\begin{align*}
& A D_1 D_2 A^{-1} \\
&= A (I + (k_1 - 1)E_{11} + (k_2 - 1)E_{22}) A^{-1} \\
&= I + (k_1-1)A E_{11} A^{-1} + (k_2-1)A E_{22} A^{-1}
\end{align*}$$

The other way,

$$\begin{align*}
& ((k_1 - 1)P_1 + I) \cdot ((k_2 - 1)P_2 + I) \\
&= (k_1 - 1)(k_2 - 1)P_1P_2 + I + (k_1-1)P_1 + (k_2-1)P_2,
\end{align*}$$

Because projecting in $P_2$, and then on $P_1$, is $0$, $P_2$ zeroes the coordinate that $P_1$ extracts later. End up with:

$$= I + (k_1 - 1)P_1 + (k_2 - 1)P_2$$

And by the previous analysis, $(k_1 - 1)A E_{11} A^{-1}$ is $P_1$, so it all makes sense algebraically.