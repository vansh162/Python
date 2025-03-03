a = input("Enter any word: ")
print(a[::-1])
if a == a[::-1]:
    print("It is a PALINDROME.")
else:
    print("It is not a PALINDROME.")