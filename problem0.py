def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_with_trace(n):
    call_trace = []  
    
    def recursive_fib(val):
        call_trace.append(f'fib({val})')

        if val == 0:
            return 0
        elif val == 1:
            return 1
        else:
            return recursive_fib(val - 1) + recursive_fib(val - 2)

    result = recursive_fib(n)
    return call_trace, result  


calls_made, result = fibonacci_with_trace(5)
print("Sequence of Calls:", " -> ".join(calls_made))
print("Final Answer:", result)
