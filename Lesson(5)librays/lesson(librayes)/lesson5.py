import os
import sys
import math
print(os.name)
print(os.getcwd())
new_path = os.path.join(os.getcwd(), 'new_f')
# os.mkdir(new_path)

print(sys.executable)
print(sys.platform)
# sys.exit()
print("Tobi P**da")
print(sys.path)
print(type(sys.path))

for p in sys.path:
    print(p)
sys.path.append("J:")
import pythonfileTEST

name = sys.platform
def mkdir():
    for i in range(1, 6):
        new_folder = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(new_folder)
def rmdir():
    for n in range(1, 6):
        del_patch = os.path.join(os.getcwd(), '{}_{}'.format(name, n))
        os.rmdir(del_patch)
rmdir()


