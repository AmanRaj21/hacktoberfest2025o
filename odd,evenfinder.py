nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
odds = [n for n in nums if n % 2 != 0]
evens = [n for n in nums if n % 2 == 0]

print("Odd numbers:", odds)
print("Even numbers:", evens)
