
import os
from random import choice
import datetime

BASE_DIR = 'C:\\Windows'


class Packer():

    counter = 0     # счетчик упаковок
    obj_count = 0

    def __init__(self, method, name='NoName', *files):
        self.method = method
        self.name = name
        self.files = list(files)
        Packer.obj_count += 1

    def pack(self):
        """Упаковка файлов
        """
        print('Упаковка...')
        Packer.counter += 1

    def __add__(self, other):  
        return Packer(self.method + '|' + other.method, 
                        self.name + '-' + other.name) 
    

    def __sub__(self, other):
        print('Я тебе вычту! Ух!')

    def __len__(self):
        return len(self.files)

    def __str__(self):
        return 'Packer {}. Method {}'.format(self.name, self.method)    
        
    # def __repr__(self):
    #     return '== {} {} {} =='.format(self.name, self.method, self.files)

    @classmethod    
    def stat(cls):
        print('Всего упаковок {}, всего объектов {}'.format(cls.counter, cls.obj_count))
        return cls.counter, cls.obj_count

    @property    
    def x_files(self):
        print('X-Files')
        files = [os.path.join(BASE_DIR, f) for f in self.files]
        return files  

    @staticmethod    
    def fast_pack(method, *files):
        for f in files:
            print('Packing {} with {}'.format(f, method)) 

    @staticmethod        
    def random_packer():
        m = choice(['zip','7z', 'rar', 'gzip', 'bz2'])
        return Packer(m)
          

class Joker():
    def smile(self, smilesize):
        print(" :) " * smilesize)    


class SuperPacker(Packer, Joker):

    def __init__(self, method):
        super().__init__(method)
        self.smilesize = 17



sp = SuperPacker('ZIP')
sp.smile(11)
        
    

dt = datetime.datetime.today()
print(dt)            


p1 = Packer('zip', 'Зипушка', 'test1', 'test2')
# print('Длина Зипушки ', len(p1))
p2 = Packer('rar', 'Рарчик')
p3 = Packer('7z')

p_1_2 = p1 + p2 + p3
# print(p_1_2)
# Packer.fast_pack('bz2', 'z1', 'z2', 'z3')
p5 = p3.random_packer()

p_list = [p1, p2, p3, p_1_2, p5]
for p in p_list:
    print(p)
# print(p_list)

# print(repr(p1))


# print('5-й:', p5.method)

# Packer.stat()
# p1.pack()
# Packer.stat()

# p4 = Packer('gzip')
# p4.stat()

# print('упаковок {}, объектов {}'.format(p4.counter, p4.obj_count))
# print('упаковок {}, объектов {}'.format(p2.counter, p2.obj_count))

# print(p1.x_files)