'''
Created on Mar 8, 2020

@author: Pavan
'''
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def get_details(self):
        print(self.id," ",self.name)
obj = Student(101,"sarath")
obj.get_details()