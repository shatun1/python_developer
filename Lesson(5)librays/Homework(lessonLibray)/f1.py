import sys, os
name = sys.platform
def make_dir():
    for i in range (1, 6):
        new_folder = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(new_folder)
def del_dir():
    for n in range(1, 6):
        del_patch = os.path.join(os.getcwd(), '{}_{}'.format(name, n))
        os.rmdir(del_patch)


