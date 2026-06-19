## K-Means

In the real world let's say that we can gather some numerical values about something, we end up with $n$ vectors where each dimension of the vector represent one kind of numerical value,

The question is: Does this vectors have a hidden group structure that makes sense to the domain experts?

K-means is an algorithm of grouping, which means that it will group the vectors in some predetermined number of groups, whether those groups makes sense have to be determined later by domain experts.

So given a number of groups $k$, and a list of vectors it will return a partition of those vectors that has $k$ groups.

What makes K-means different from an algorithm that will chose one of the finite partitions with $k$ groups that can be created from the list of vectors.

Interesting question: Can there be an algorithm that uniformly random returns a partition given $k$, and the list of vectors, even tough the number of partitions is a big number.

Shouldn't be because else this algorithm could be used to start the K-means algorithm and it's not used, also the sample space contains an exponential number of elements.

Let's say that there is an initial partition $P = \{G_1, G_2, \dots, G_k\}$ of a list of vectors $V$ that has $k$ sets.

One metric $M$ about a group $G$ is the sum of the squared distances of each vector to the average vector.

$$A_G = \frac{\sum_{x \in G} x}{G}$$

$$M_G = \sum_{x \in G} \|x - A_G\|^2$$

If we sum this metric over the groups, we get a metric about the partition

$$\sum_{g \in P} M_g = \sum_{g \in P} \left(\sum_{x \in g} \|x - A_g\|^2\right)$$

K-means is an algorithm that iteratively tries to improve this metric by finding partitions that have strictly smaller value of the metric.

In every iteration it performs two steps.

One step is that given a partition with $k$ sets, this determines $k$ average vectors, K-means creates another partition assigning every vector the average vector closest to it. This can only improve the metric, since if a vector changes its assigned vector is because there is one closest.

Then again, we have a partition, but because this is different we may have new the average vectors, and consequently the metric value may have changed.

This step improves the metric again, and the reason is the following:

At this point, the vectors in every group have assigned a vector (the previous average vector), which could or not could be the actual average vector of a group (after the step of reassigning).

Fact: Given a list of vectors $V$, and a vector $v$, we can compute:
$$\sum_{x \in V} \|x - v\|^2$$

The question is for which $v$ is that sum minimized, it turns out that if $v$ is the average vector of $V$, then that sum is minimized.

It's because:
$$\begin{align}
\sum_{x \in V} \|x - v\|^2 &= n\|v\|^2 + \left(\sum_{x \in V} \|x\|^2\right) - 2v \cdot \left(\sum_{x \in V} x\right)
\end{align}$$

Which means to minimize the following:
$$\begin{align}
n\|v\|^2 - 2v \cdot \left(\sum_{x \in V} x\right) &= n\|v\|^2 - 2n v \cdot P \\
&= \|v\|^2 - 2v \cdot P
\end{align}$$

How prove that $v = P$ is the minimum?, if $v$ were a vector with only one coordinate it's a matter of differentiate and find the zero of the function, but is this still valid when $v$ has more than one dimension?

With that lemma / result, can be seen why that step improves the metrics.

K-means applies those two steps one after the other in a loop, so the question is what makes it stop?

Those two steps have two outcomes:
- decrease the metric, finding a new partition
- nothing changes

This means that either the algorithm get stuck in a partition or it finds a new one with smaller metric than the previous one. Because there are a finite number of partitions and the algorithm builds a strictly decreasing sequence of partitions (sorted by its metric) it can't run indefinitely.

From the greedy perspective, there are some conclusions:

- it may take exponential steps to finish.
- The actual value of the metric is irrelevant, moreover what's the difference between two partitions whose metric differ by any quantity.

The K-means problem is about given a list of vectors and a number $k$, find the partition that has the smallest value of the metric. The greedy algorithm can ensure it finds it, cause it getting stuck doesn't mean it found the best partition.

A question is what will be the type of data where applying K-Means could be adequate? From the way the algorithm works, I guess that should be groups that can be enclosed in balls, so that disjoint balls can be deduced.

Two questions that don't have a definitive answer (there are different ways of doing it):

- how define the initial partition.
- what's a correct number of groups.
