

class CheckType:
    def __int__(self):
        print('999')
        pass

    # def __set_name__(self, owner, name):
    #     self.name = name

    def __set__(self, instance, value):
        # print('set',instance.__dict__,instance,value)
        instance.chinese = value

        # instance.__dict__[self.name] = value
    def __get__(self, instance, owner):
        # print('get')
        pass
    def __delete__(self, instance):
        pass



class Student:
    chinese = CheckType()
    english = CheckType()


    def __init__(self,name,chinese,english):
        self.name = name
        self.chinese = chinese
        self.english = english


    def __repr__(self):

        return  'student:{} chinese:{} eng:{}'.format(self.name,self.chinese,self.english)


stu = Student('jack',60,70)

print(stu)
print(stu.__dict__)
