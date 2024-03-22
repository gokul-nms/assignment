number = int(input("Enter the number: "))
odd = 0
even = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        even += digit
    else: 
        odd += digit
    number //= 10

print("Sum of odd digits:", odd)
print("Sum of even digits:", even)
