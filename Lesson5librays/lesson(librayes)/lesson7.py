import sys, os
# for arg in sys.argv:
#     print(arg)
#     print(type(arg))
def ping():
    print('pong')


def hello(name):
    print('Hello', name)

hello('Nikita')

def get_info():
    print(os.listdir())

command = sys.argv[1]
if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)
