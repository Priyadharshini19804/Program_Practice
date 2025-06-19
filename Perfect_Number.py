'''

Write code of  Perfect number 
 A perfect number is a positive integer that is equal to the sum of its proper divisors, 
excluding the number itself.  
 Example: Is 28 a perfect number? 
The divisors of 28 are 1, 2, 4, 7, 14. 
Sum of divisors: 1 + 2 + 4 + 7 + 14 = 28, so 28 is a perfect number.

'''

n = int(input("Enter a number: "))
Sum = 0
for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
if (Sum == n):
    print(f"{n} is a Perfect Number.")
else:
    print(f"{n} is not a Perfect Number.")
