import os
def make_dir(*s):
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), i)
        try:
            os.mkdir(dir_path)
            print('директория {} создана'.format(i))
        except FileExistsError:
            print('директория {} уже существует'.format(i))