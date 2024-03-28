# Calculate the sum of all the digits in a number

def sum_of_degits(digit):

    # Convert digit to string
    string = str(digit)

    sum = 0

    for i in range(len(string)):
        sum += int(string[i])
    print(f"Sum: {sum}")

digit = 2021     
sum_of_degits(digit)

# Output
# Sum: 6


 