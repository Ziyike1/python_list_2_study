for value in range(1,5):
    print(value)
print("\n")

for value in range(1,6):
    print(value)
print("\n")

for value in range(8):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_number = list(range(2,11,2))
print(even_number)

odd_number = list(range(1,11,2))
print(odd_number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表推导式
squares = [value**2 for value in range(1,11)]
print(squares)