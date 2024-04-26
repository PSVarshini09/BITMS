'''import math
print('the value of pi is',math.pi)'''

'''import math as m
print(m.pi)'''

'''import sathyasaimodule
print(sathyasaimodule.varshini())'''

'''from datetime import date
print('today date',date.today())'''

'''import os
os.mkdir("d:\\tempdir")
os.chdir("d:\\temp")
os.getcwd()
'd:\\
os.rmdir("d:\\temp")'''


#use pass inside if statement
'''n=10
if n>10:
    pass
    print('test')
else:
    print('take care')'''

#abstractmethod
from abc import ABC,abstractmethod
'''class Car(ABC):
    def mileage(self):
        pass
    def bitm_mileage(self):
        print('non abstract method')
class tesla(Car):
    def mileage(self):
        print('tesla speed is 130kmph')
class duster(Car):
    def mileage(self):
        print('duster speed is 120kmph')
t=tesla()
t.mileage()
d=duster()
d.mileage()'''
        