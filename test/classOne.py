class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._gae


    @age.setter
    def age(self,age):
        self._age=age


    def play(self):
        if self._age<=16:
            print('%s正在玩飞机'%self._name)
        else:
            print('%s正在玩斗地主'%self._name)


person =Person('王大锤',22)
person.play()