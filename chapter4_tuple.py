dimensions = (200,500)
print(dimensions)
print(dimensions[0])
# dimensions[1]=100

single_tuple = (1,)
print(single_tuple)

#元组不需要圆括号
single_tuple = 1,
print(single_tuple)

print("\nOriginal dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400,600)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)