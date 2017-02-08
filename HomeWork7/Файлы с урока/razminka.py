
# x = 1


# class c:
#     x = 2
#     print('Я первый', x)
#     def m(self):
#         print('я внутри', x)


# print('я последний', x)
# i = c()
# i.m()

# ------------------------------------

class BaseClass():
    x = 1
    y = 2


class ChildClass(BaseClass):
    x = 111
    y = 222

    def mix(self):
        return self.__class__.y


c = ChildClass()

print(c.mix())        
print(BaseClass.y)
print(ChildClass.y)




