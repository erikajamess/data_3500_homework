#3.4
for i in range (2): #looping a new line twice
    for j in range(7): #loop :) 7x
        print(':)', end='')#end= is putting it on the new line.
    print() # in the first loop, creating the new line


#3.9
# Ask the user for a number (7–10 digits)
num = int(input("Enter a number 7 to 10 digits: "))
# We will keep looping until there are no digits left
while num > 0:
    # Get the rightmost digit
    digit = num % 10
    # Print the digit
    print(digit)
    # Remove the rightmost digit
    num = num // 10

total_miles = 0
total_gallons = 0

# Ask the user for gallons used (sentinel value is -1)
gallons = float(input("Enter the gallons used (-1 to end): "))
while gallons != -1:
    # Ask for miles driven for this tank
    miles = float(input("Enter the miles driven: "))

    # Calculate miles per gallon for this tank
    mpg = miles / gallons

    # Display the MPG for this tank
    print(f"The miles/gallon for this tank was {mpg:.6f}")#allows for 6 digits. 

    # Add this tank's values to the totals
    total_miles += miles
    total_gallons += gallons

    # Ask for gallons again (next loop or sentinel)
    gallons = float(input("Enter the gallons used (-1 to end): "))

# After the loop ends, calculate overall MPG if any data was entered
if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was {overall_mpg:.6f}")

#3.12
#Create a variable, which stores user input. Prompt the user to enter a 5 digit number.
variable = int(input('Please enter a 5 digit number:' ))
#To get the first digit alone, floor division by 100. 
first = variable // 10000

last = variable % 10

num = variable // 1000
second = num % 10

dig = variable // 10
fourth = dig % 10

if first == last and second == fourth:
  print('Palindrome!')
else: 
  print('not a palindrome!')

#3.14
# Some parts of this code were written with the help of ChatGPT.
# I used it to better understand the formatting and calculations



#how many iterations we will have
MAX_ITERS = 3000
# This will store our running approximation of pi
pi_approx = 0.0
# sign controls whether we add or subtract the next term
# Start with +4/1
sign = 1

# denominator starts at 1 and increases by 2 each term 
denom = 1
# Counters to track how many times we've seen the target strings
count_314 = 0
count_3141 = 0
# These will store the iteration number when we see the value the 2nd time
second_time_314 = None
second_time_3141 = None

# Main loop: add one term each iteration
for i in range(1, MAX_ITERS + 1):
    # Compute the next term: 4/denom, with alternating sign
    term = sign * (4 / denom)
    # Add term to our running total
    pi_approx += term
    # Flip the sign for the next iteration (+ then - then + then - ...)
    sign *= -1
    # Increase denominator by 2 to get the next odd number
    denom += 2

    # Convert to strings the SAME way print formatting would (this rounds)
    pi_2dp = f"{pi_approx:.2f}"
    pi_3dp = f"{pi_approx:.3f}"

    # Print the table row
    print(f"{i}\t{pi_approx:.10f}\t{pi_2dp}\t\t{pi_3dp}")
    # Track when 3.14 appears
    if pi_2dp == "3.14":
        count_314 += 1
        # If this is the second time we've seen it, record the iteration
        if count_314 == 2 and second_time_314 is None:
            second_time_314 = i

    # ---- Track when 3.141 appears (to 3 decimals) ----
    if pi_3dp == "3.141":
        count_3141 += 1
        # If this is the second time we've seen it, record the iteration
        if count_3141 == 2 and second_time_3141 is None:
            second_time_3141 = i

# After the loop, print out what we found.
print("\nSummary:")
print(f"2nd time pi shows as 3.14 (2 decimals in our iterations:{second_time_314}")
print(f"2nd time pi shows as 3.141 (3 decimals in our iterations: {second_time_3141}")
