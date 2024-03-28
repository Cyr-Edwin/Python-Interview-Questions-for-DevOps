# Find the Fibonacci sequence

def fibonacci(n):

    # Start
    if n in [1,2]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Fibonacci sequence starts with 1
print(f"Finobacci sequence: \n")
for i in range(1 ,10):
    print(f"{fibonacci(i)}")

# Output:

#Finobacci sequence: 

# 1
# 2
# 3
# 5
# 8
# 13
# 21
#34
#5
 