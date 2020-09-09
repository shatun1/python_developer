friend = 'Ilya NIkita1'
word_number = friend[-2]
print(word_number)
print(friend[:2])
print(friend[1:3])
print(len(friend))#узнать кол-во символов
print(friend.find('Il'))#найти номер символа, с которого начинается подстрока
print(friend.split(';'))
print(friend.isdigit())#Проверка строки на состав цифр
number = "123"
print(number.isdigit())
print(friend.upper())#Привести строку к верхнему регистру
print(friend.lower())#Привести строку к нижнему регистру
name = 'Alex'
age = 32
hello_str = 'Привет {} тебе {} лет ' .format(name, age)
print(hello_str)
top5 = ("Вот список людей, занявших призовые места:Алексеев 1. Иванов 2. Фёдоров 3. Измайлов 4. Щетинский")
start = top5.find('1')
end = top5.find('4')
top3  = top5[start: end]
result = 'Поздравляем {} с  успехом!' .format(top3.upper())
print(result)



