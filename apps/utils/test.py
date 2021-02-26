class Typed:



    def __init__(self,type):
        self.type = type
        print('2222')



    def __set_name__(self, owner, name):
        print(name)
        self.public_name = name
        self.private_name = '_' + name
        print(self.__dict__)


    def __set__(self, instance, value):

        if not isinstance(value,self.type):
            raise ValueError(value)
        setattr(instance, self.private_name, value)

    def __get__(self, instance, owner):
        value = getattr(instance,self.private_name)
        #
        return value





class Student:
    chinese = Typed(float)
    math = Typed(float)
    def __init__(self, name:str,chinese:float, math:float):
        self.name = name
        self.chinese = chinese
        self.math = math
        print('1111')

    def __repr__(self):

        return "student name:{} chinese:{} math:{}".format(self.name,self.chinese,self.math)


c = Student('tom',66.3, 80.5)

c2 = Student('tom3',99.9, 80.5)

print(c)
print(c2)


