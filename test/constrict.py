class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

dart=Student("奇偶",100)
print(dart.name) 
print(dir(dart))      