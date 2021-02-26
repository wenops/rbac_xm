from django.test import TestCase

# Create your tests here.
# d = {'a':123,'b':456,'c':999}
# # for i in d:
# #     print(d[i])
# d.update({'d':000})
#
# print(d)

# class Person:
#     def normal_method():
#         print('normal')
#
#     def method(self):
#         print("{}'s method ".format(self))
#
#     @classmethod
#     def class_method(cls):
#         print('class = {0.__name__}({0})'.format(cls))
#         cls.HEIGHT = 170
#
#     @staticmethod
#     def static_method():
#         print(Person.HEIGHT)
#
#
#
# print('~~~类访问')
# print(1,Person.normal_method())
# print(2,Person().method())
# print(3,Person.class_method())
# print(4,Person.static_method())
# print(Person.__dict__)
#
#
#
#
#
#
# Person.normal_method()


# d = {'a':123,'b':456,'c':999,'tom':{'age':'111','son':[]}}
# # for i in d:
# #     print(d[i])
# e = d['tom']
# e['son'].append('666')
#
# print(d)

class MyClass:

    def __init__(self,score):
        self._score = score

    @property
    def get_sc(self):

        return self._score


class MyClassA(MyClass):


    def get_sc(self):
        return  self._score + 10

cl = MyClass(99)
cl._score = 50
# cl.__dict__['_MyClass__score'] = 66
print(cl.__dict__)
print(MyClass.__dict__)
print(cl.get_sc)


cla = MyClassA(88)
print(cla.get_sc())



