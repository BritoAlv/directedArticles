## K-Means

In the real world let's say that we can gather some numerical values about something, we end up with n vectors where each dimension represent a metric, 

The question is: Does this vectors have a hidden groups structure that makes sense to the domain experts?

K-means is an algorithm of grouping, which means that it will group the vectors in some predetermined number of groups, whether those groups makes sense have to be determined later by domain experts.

So given a number of groups k, and a list of vectors it will return a partition of those vectors that has k groups.

What makes K-means different from an algorithm that will chose one of the finite partitions with k groups that can be created from the list of vectors. 

Interesting question: Can there be an algorithm that uniformly random returns a partition given k, and the list of vectors, even tough the number of partitions is a big number. 

Shouldn't be because else this algorithm could be used to start the K-means algorithm and it's not used, also the sample space contains an exponential number of elements.

Coming back to K-Means the thing about it is that is good at creating groups that are enclosed in a ball.

Let's say that there is an initial partition P of a list of vectors V that has k sets.

One metric about a group is the distance of each vector to the average vector.

If we take this metrics over the groups, and sum those values, we get a metric about the partition, K means is an algorithm that iteratively tries to improve this metric.

One step is that given a partition with k sets, this determines k average vectors, K-means creates another partition assigning every vector the average vector closest to it. This improves the metric, since if a vector changes its assigned vector is because there is one better.

Then again, we have a partition, but because this is different we have to update the average vectors, and consequently update the metric. 

This step improves the metric again, and the reason is the following:

At this point, the vectors in a group have assigned a vector, which could or not could be the actual average vector of a group.

Fact: Given a list of vectors V, and a vector v, we can compute:
    sum x in V d(x - v)^2

The question is for which v is that sum minimized, it turns out that if v is the average vector of V, then that sum is minimized.

It's because:
        sum x in V d(x - v)^2
    = n|v|^2 + (sum x in V |x|^2) - 2v (sum x in V x)

Which means to minimize the following:
    n|v|^2 - 2v (sum x in V x)
    n|v|^2 - 2n v P
    |v|^2 - 2v P

How prove that v = P is the minimum?, if v were a vector with only one coordinate it's a matter of differentiate and find the zero of the function, but is this still valid when v has more than one dimension?

With that lemma / result, can be seen why that step improves the metrics.

K-means applies those two steps one after the other in a loop, so the question is what makes it stop?

Those two steps have two outcomes:
    - decrease the metric, creating a new partition
    - nothing changes
  
This means that either the algorithm get stuck in a partition or it finds a new one with smaller metric than the previous one. Because there are a finite number of partitions the algorithm can't run indefinitely.

From the greedy perspective, there are some conclusions:

    - it may take exponential steps to finish
    - the actual value of the metric is irrelevant, moreover what's the difference between two partitions whose metric differ by any quantity.

The K-means problem is about given a list of vectors and a number k, find the partition that has the smallest value of the metric. Which the greedy algorithm can ensure it finds it, cause it getting stuck doesn't mean it found the best partition. 

A question is what will be the type of data where applying K-Means could be adequate? From the way the algorithm works, I guess that should be groups that can be enclosed in balls, so that disjoint balls can be deduced. 

Two questions that don't have a definitive answer (there are different ways of doing it):

    - how define the initial partition
    - what's a correct number of groups