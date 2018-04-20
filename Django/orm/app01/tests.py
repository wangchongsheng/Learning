from django.test import TestCase

# Create your tests here.


class Person():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
obj=Person("csking")
print(obj)
