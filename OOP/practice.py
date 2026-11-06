

class Student:
    school = "PSU"

    def __init__(self, name, course="BSIT", age=0):
        self.name = name
        self.course = course
        self.age = age

    

    @classmethod
    def display_school(cls):
        print(cls.school)


    @staticmethod
    def grade(grade):
        print(grade)
    def print_student(self):
        print(self.name)
        print(self.course)
        print(self.age)

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name






