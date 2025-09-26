  # Fibonacci Sequence Program

# Function to generate Fibonacci sequence
def fibonacci(n):
    n1, n2 = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(n1)
        n1, n2 = n2, n1 + n2
    return sequence

print("Fibonacci Sequence program")
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(terms)
    print("Fibonacci sequence:")
    #Display the sequence 
    for num in result:
        print(num, end="  ")
        
