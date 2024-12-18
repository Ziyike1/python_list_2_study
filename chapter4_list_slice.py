players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:-3])

#每隔(2-1 = 1)个元素提取一次 ['charles', 'michael']
print(players[0:4:2])

print("Here are the first three players in the team")
for player in players[:3]:
    print(player)

#复制整个列表，使用切片的方式
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]
# print(f"my food are:{my_food}")
# print(f"friend's food are:{friend_food}")