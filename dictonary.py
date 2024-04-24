# the data is stored as key-value pairs using a python dictionary
'''emp={"name":"varshini","age":30,"salary":250000,"dob":"2004-09-06"}
print("employee data...")
print(emp)'''

#creating a dictionary using dict method
'''Dict=dict({1:'mango',2:'apple',3:'banana'})
print(Dict)'''

#with item as a each pair
'''Dict=dict([(4,'varshini'),(2,'abc')])#tuple to dictionary
print(Dict)'''

'''emp={"name":"varshini","age":30,"salary":250000,"dob":"2004-09-06"}
print("employee data...")
print(type(emp))
print('name:%s'%emp['name'])
emp['emp_ages']=20,33,44#adding one more element
print(emp)'''

'''emp={1:"varshini",2:30,"salary":250000,3:"2004-09-06"}
print("employee data...")
print(type(emp))
pop_keys=emp.pop(2)
print(emp)'''

'''emp={"name":"varshini","age":30,"salary":250000,"dob":"2004-09-06"}
print("employee data...")
print(type(emp))
print('enter the details of new employee')
emp['name']=input('name:');
emp['age']=int(input('age:'));
print(emp)'''


#working of functions as dictionary values using without params
'''def varshini():
    return 'this is my bank balance'
test_dict={'fname':varshini,'age':18,'address':'salem'}
print('the original dictionary is:'+str(test_dict))
res=test_dict['fname']()
print('the required call result:'+str(res))'''


'''def varshini(a,b):
    print(a+b)##print('my bank balance',a+b)
test_dict={'fname':varshini,'age':18,'address':'salem'}
print('the original dictionary is:'+str(test_dict))
test_dict['fname'](10,20)'''


