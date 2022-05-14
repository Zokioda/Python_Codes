# Program to reverse a number....

n = int(input("Enter a number that is to be reversed : "))
rev = 0
is_postive: bool = False
if n < 0:
    n = n * -1
    is_postive = True
while n > 0:
    # Get the Last digit of the number
    last_digit = n % 10
    # add the last digit to the number
    rev = rev * 10 + last_digit
    # Changing the original number so that we can get other last digit from it
    n = n // 10

if is_postive:
    rev = rev * -1
print('The number after reversing is :', rev)
