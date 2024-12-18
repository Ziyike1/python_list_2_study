#4.1
my_favorite_pizza = ["cheese","beef","chicken","fruit"]

for pizza in my_favorite_pizza:
    print(pizza)
    print(f"I like {pizza} pizza.\n")

print("I really love pizza!\n")


#4.2
animals = ["cat","dog","bird"]

for animal in animals:
    print(animal)
    print(f"A {animal} would make a great pet.\n")

print("Any of those animals would make a great pet!")


#4.3
for value in range(1,21):
    print(value)


#4.4
my_list = list(range(1,1000001))
for value in my_list:
    print(value)


#4.5
my_list = list(range(1,1000001))
print(min(my_list))
print(max(my_list))
print(sum(my_list))


#4.6
my_odd_list = list(range(1,21,2))
for value in my_odd_list:
    print(value)


#4.7
my_three_list = list(range(3,31,3))
for value in my_three_list:
    print(value)


#4.8
my_third_list = []
for value in range(1,11):
    my_third_list.append(value**3)
print(my_third_list)


#4.9
my_third_list = [value**3 for value in range(1,11)]
print(my_third_list)


#4.10
my_list = [1,2,3,4,5,6,7,8,9,10]
print(f"The first three item in the list are: {my_list[:3]}")
print(f"The middle three item in the list are: {my_list[3:6]}")
print(f"The last three item in the list are: {my_list[-3:]}")


#4.11
my_favorite_pizza = ["cheese","beef","chicken","fruit"]
friend_pizza = my_favorite_pizza[:]
my_favorite_pizza.append("original")
friend_pizza.append("italian")

for pizza in my_favorite_pizza:
    print(pizza)
    print(f"I like {pizza} pizza.")

print("I really love pizza!\n")

for pizza in friend_pizza:
    print(pizza)

    print(f"My friend like {pizza} pizza.")

print("My friend really love pizza!\n")


#4.12
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]
for food in my_food:
    print(food)

for food in friend_food:
    print(food)

my_food.append("ice")
friend_food.append("cream")
print(f"my food are:{my_food}")
print(f"friend's food are:{friend_food}")


#4.13
res_menu = ('snack','seafood','rice','egg','apple')
for food in res_menu:
    print(food)
print('\n')

res_menu = ('snack','seafood','rice','water')
for food in res_menu:
    print(food)