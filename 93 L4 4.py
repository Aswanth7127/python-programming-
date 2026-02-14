num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i
is_perfect = (sum_factors == num)
order = len(str(num))
sum_armstrong = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_armstrong += digit ** order
    temp //= 10
is_armstrong = (sum_armstrong == num)
is_palindrome = (str(num) == str(num)[::-1])
square = num * num
is_automorphic = str(square).endswith(str(num))
print("Prime:", is_prime)
print("Perfect:", is_perfect)
print("Armstrong:", is_armstrong)
print("Palindrome:", is_palindrome)
print("Automorphic:", is_automorphic)
