friend = "Саня"
print((friend))
print(type(friend))
first_letter = friend[0]
print('First word of name is', first_letter )
print(type(first_letter))
print(friend[-1])
print(friend[:2])
print(friend[1:3])
print(friend[2:])
print(type(friend[1:3]))
friends = "Саша Никита"
print(friends)
print(len(friends))
print(friends.find("Са"))
print(friends.split())
friends = "Саша;Никита"
print(friends.split(" ; "))
print(friends.isdigit())
number = '223'
print(number.isdigit())
print(friend.upper())
print(friend.lower())
name = "nikita"
age = 16
hello_str = "Привет {} тебе {} лет".format(name, age)
print((hello_str))

top5 = "Первые 5 мест на соревнованиях: 1. Иванов. 2. Петров. 3.Сидоров. 4. Орлов. 5. Соколов. "
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
print((top3))
result = "Поздравляем {} с успехом!".format(top3.upper())
print((result))





