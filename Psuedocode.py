def largest_number(x, y):
    if x > y:
        return x
    else:
        return y
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(largest_number(x, y))

