list = [1,2,3,4,5,6,7,8,9]
for number in list:
    print(number)

# 以下方法用于复制一个完整的列表
other_list = list[:]
print(other_list)

# range(1,101,2) 表示从1到100，中间隔两个数
number_list = []
for value in range(1,101,2):
    number_list.append(value)
print(number_list)

#列表推导式
number_list = [value for value in range(1,101,2)]
print(number_list)

# min(),max(),sum() 方法用于找出列表的特定最值
print(min(number_list))
print(max(number_list))
print(sum(number_list))

# [-3:] 表示从倒数第三个数开始向后数
print(number_list[-3:])
print(number_list[:-3])

my_tuple = (1,3,5,7)
print(my_tuple)
my_tuple = (5,6,7)
print(my_tuple)