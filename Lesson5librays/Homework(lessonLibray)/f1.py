import sys, os
name = sys.platform
def make_dir():
    for i in range (1, 10):
        # new_folder = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        new_folder = f'dir_{i}'
        os.mkdir(new_folder)
def del_dir():
    for n in range(1, 10):
        # del_patch = os.path.join(os.getcwd(), '{}_{}'.format(name, n))
        del_folder = f'dir_{n}'
        os.rmdir(del_folder)


