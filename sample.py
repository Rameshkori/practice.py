# create assending ordera = 53 , 21 , 23
# a=53
# b=21
# c=23
# print(sorted([a, b, c])) 

a=21
b=42
print(a + b)

# create polindrome number
num = 121
temp = num
reverse = 0
while (num > 0):
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
if (temp == reverse):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")