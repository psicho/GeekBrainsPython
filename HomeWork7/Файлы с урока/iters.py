

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(self.data)

    def __str__(self):
        return 'я - итератор'

    def __iter__(self):
        return self
        
    def __next__(self):     # Python 2:  next()        
        self.index -= 1
        if self.index > -1:
            return self.data[self.index]
        else:
            self.index = len(self.data)     # хитрость от Максима :)
            raise StopIteration 


r = Reverse('abcdef')            
print(r)

ls = (i for i in r)
# print('r', list(r))
# print('ls', list(ls))

print(dir(ls))

for i in ls:
    print(i)

next(ls)
