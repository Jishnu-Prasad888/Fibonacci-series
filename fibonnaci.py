def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Calculate subsequent Fibonacci numbers
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence[:n]

# Get user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Calculate and print the Fibonacci series up to nth number
fib_series = fibonacci(n)
print(f"Fibonacci series up to {n} numbers:", fib_series)
