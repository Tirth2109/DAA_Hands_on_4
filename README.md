Problem 0

Implement the Fibonacci sequence

x = fib(n)

    if n == 0

        return 0

    if n == 1

         return 1

    return fib(n-1) + fib(n-2)

Debug the code and "step into" the function for fib(5). I want you to step into all recursive calls and list out the the function call stack ex. fib(5) -> fib(4) -> fib(3) ?....  that you observe.

Note, don't turn on optimization if your programming language allows it.

Another note make sure to implement the return exactly as

return fib(n-1) + fib(n-2) instead of say

a = fib(n-1)

b = fib(n-2)

return a + b

OR as

return fib(n-2) + fib(n-1)

The reason is, I want everyone to have similar results.

 

For the following two problems:

1. Implement the solutions and upload it to github
Answer: problem.py

3. Prove the time complexity of the algorithms.
Answer: In the naive Fibonacci implementation, each call to fib(n) results in two additional recursive calls, creating a tree-like structure of function invocations. At each recursive step, two branches are generated, representing the two recursive calls made at that level. This forms a binary recursion tree that grows rapidly as the input size increases.
The number of calls made at each level of this recursion follows a pattern of powers of 2. Specifically, at the nth level, there are 2n2^n2n calls. Thus, the total number of recursive function calls is proportional to 2n2^n2n, representing an exponential growth in the number of operations required.
In terms of time complexity, this behavior is expressed as O(2n)O(2^n)O(2n). This signifies that the runtime of the algorithm increases exponentially as the input nnn grows. This exponential increase makes the algorithm inefficient for larger values of nnn, primarily due to a significant amount of repeated calculations.

4. Comment on way's you could improve your implementation.
Answer: The basic Fibonacci algorithm is inefficient for larger nnn because of its exponential time complexity, caused by repeated recursive calls and redundant calculations. The recursive structure leads to significant overhead as the same Fibonacci values are computed multiple times.
To improve efficiency, memoization or dynamic programming can be applied. These techniques store previously computed results in a data structure, such as an array or dictionary, and reuse them when needed, preventing redundant calculations. By doing so, the time complexity is reduced to O(n)O(n)O(n), making the algorithm much faster and more suitable for larger inputs

