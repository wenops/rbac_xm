class Typed:

    def __init__(self,type,name):
        self.type = type
        #name 存储变量
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value,self.type):
            raise ValueError(value)
        instance.__dict__[self.name] = value


    def __get__(self, instance, owner):
        value = instance.__dict__[self.name]
        return value

#类中实现检查(inpsect)
import inspect
class TypeAssert:

    def __init__(self,cls):
        self.cls = cls
        params = inspect.signature(self.cls).parameters
        for name, param  in params.items():
            # print(name, param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls,name,Typed(param.annotation,name)) #注入类属性

                print(Typed.__dict__)


    def __call__(self, name,chinese,math):
        p = self.cls(name,chinese,math)
        return  p

@TypeAssert
class Student:

    def __init__(self, name:str,chinese:float, math:float):
        self.name = name
        self.chinese = chinese
        self.math = math

    def __repr__(self):

        return "student name:{} chinese:{} math:{}".format(self.name,self.chinese,self.math)


c = Student('tom',66.3, 80.5)
c2 = Student('jack',80.6,66)

print(c,c2)

