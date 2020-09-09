def hello_max():
    print('hello, max')
hello_max()

def hello(who):
    print('hello', who)
hello('Leo')

def greeting(say, *args):
    print(say, args)
greeting('HI', 'NIK', 'Leo', 'Sanya', 'DANYA')

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
get_person(name='Leo', age=20)















