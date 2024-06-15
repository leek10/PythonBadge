# Solving Project Euler Problems
# Problem 1: Finding the sum of all the multiples of 3 or 5 below 1000 (goal: 233168)

numberList = [3,5]          # defining list
maxNumber = 1000
sumNumbers = 0
for n in range(0,maxNumber):
    if n%3 == 0 or n%5 == 0:    # NumberModNumer == remainder
        sumNumbers += n       # adds to total sum
print("Problem 1 answer:",sumNumbers)


# Problem 2: Finding the sum of the even valued terms of the Fibonacci sequence values under 4 million (goal: 4613732)

termCur,termPrev = 1,1              # defining start of the Fibonacci sequence
sumNumbers = 0      
while termCur <= 4000000:
    if termCur%2 == 0:
        sumNumbers += termCur   
    termCur += termPrev             # Moves onto the next number in the sequence
    termPrev = termCur - termPrev   # Moves the previous number to the next number in the sequence

print("Problem 2 answer:",sumNumbers)


# Problem 3: Finding the largest prime factor of the number 600851475143 (goal: 6857)

number = 600851475143
factorList = []                     # creates a list of factors
divisor = 2                         # starting divisor
while number > 1:
    while number%divisor == 0:      # remainder of 0 
        factorList.append(divisor)  # adds number to list
        number /= divisor           # divides number by divisor and runs through again
    divisor += 1
print("Problem 3 answer:",max(factorList))
