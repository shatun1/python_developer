
#n = n+2;
#print(n);
while True:
    n = int(input('Введите число больше нуля, но меньше 10'))
    if n in range(0, 10):
        print(n)
        break
    else:
        print("Введите верное число, оно должно состоять из одного символа.")
print(n ** 2)

