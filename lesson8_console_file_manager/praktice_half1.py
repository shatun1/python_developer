import os
import shutil
import datetime
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')

def get_list(Folders_only = False):
    result = os.listdir()
    if Folders_only:
        result = [f for f in result if os.path.isdir(f)]
        print(result)
    print(os.listdir())

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка, которую вы хотите скопировать уже существует')
    else:
        shutil.copy(name, new_name)

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def change_dirrectory(path):
    try:
        os.chdir(path)
    except FileNotFoundError :
        print('Вы ввели неправильный путь или название папки')

if __name__ == '__main__':
    create_file('test.dat')
    create_file('test.dat', 'some text')
    create_folder('new_f')
    get_list(True)
    # delete_file("new_f")
    # delete_file('test.dat')
    copy_file('new_f', 'new2')
    copy_file('test.dat', 'test1.dat')
    print(os.getcwd())
    change_dirrectory('new2')
    print(os.getcwd())
    save_info('NNN')


