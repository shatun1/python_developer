import sys
from praktice_half1 import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dirrectory
from ugadaika_practice import ugadaika_game
save_info('start')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести имя функции')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Имя файла или папки указано неверно')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Имя файла или папки указано неверно')
        else:
            copy_file(name, new_name)

    elif command == 'change_dir':
        try:
            path = sys.argv[2]
        except IndexError:
            print('Название директории указано неверно')
        else:
            change_dirrectory(path)
    elif command == 'ugadaika':
        ugadaika_game()
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файлов')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
    save_info('finish')