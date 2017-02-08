
import time
from functools import wraps

def log(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        ''' Я декоратор простой. Что мне дали, то и залоггировал
        '''
        res = func(*args, **kwargs)
        print('Log: {}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
        return res
    # decorated.__name__ = func.__name__  
    # decorated.__doc__ = func.__doc__  
    return decorated    


def time_it(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        ''' Я декоратор простой. Что мне дали, то и обернул
        '''
        start = time.time()
        res = func(*args, **kwargs)
        delta = time.time() - start
        print('Function {} worked {}'.format(func.__name__, delta))
        return res
    # decorated.__name__ = func.__name__  
    # decorated.__doc__ = func.__doc__  

    return decorated      


@log
def my_sum(a, b):
    res = a + b
    return res

@log
@time_it
def my_mul(a, b):
    ''' Космическое умножение
    '''
    return a * b

print(help(my_mul))    

MAXI = 1000000

@time_it
def str_concat(maxi):
    s = ''
    for i in range(maxi):
        s += ' ' + str(i)
    return s
    
@time_it
def str_join(maxi):
    str_list = []
    for i in range(maxi):
        str_list.append(str(i))
    return ' '.join(str_list)    


str_concat(MAXI)
str_join(MAXI)

# my_mul = log(time_it(my_mul))

# my_sum = log(my_sum)
# @log

# print(my_mul(11, 19))

# res = my_sum(11, 7)    
# print(res)

# res = my_sum(3, 9)    
# print(res)
