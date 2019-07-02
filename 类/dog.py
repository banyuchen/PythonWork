# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title() + "is now sitting")
#
#     def roll_over(self):
#         """模拟小狗被命令是打滚"""
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
#
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dos is " + str(my_dog.age) + " years old.")

# 多态
import abc

class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass


class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')


class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')


class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')


peo=People()
dog=Dog()
pig=Pig()

#peo、dog、pig都是动物,只要是动物肯定有talk方法
#于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
# peo.talk()
# dog.talk()
# pig.talk()

#更进一步,我们可以定义一个统一的接口来使用
def func(obj):
    obj.talk()


func(peo)
func(dog)
func(pig)