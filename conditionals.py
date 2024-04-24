'''if(5>10):
    print("yes")
else:
    print("no")'''
'''age1=int(input("enter the age1"))
age2=int(input("enter the age2"))
if(age1>age2):
    age3=age1+age2
    print('my age added',age3)
else:
    age3=age1-age2
    print('my age subtracted',age3)'''
'''email='varshiniyadav319@gmail.com'
password='123456'
uemail=str(input('enter email id'))
upassword=str(input('enter password'))
if(email==uemail):
    if(password==upassword):
        print('login success')
    else:
        print('loginfailed due to incorrect password')
else:
    print('login failed due to incorrect email')'''
'''email='varshivarshini24@gmail.com'
password='123456'
otp='4567'
uemail=str(input('enter email id'))
upassword=str(input('enter password'))
uotp=str(input('enter otp'))
if(email==uemail and password==upassword):
    print('login success')
    
    if(uotp==otp):
        print('transaction successful')
    else:
        print('not successful')
else:
    print('login failed')'''
'''num1=int(input("enter num1"))
num2=int(input("enter num2"))
if(num1>num2):
    print('num1 is greater')
elif(num1==num2):
    print('num1 and num2 are equal')
else:
    print('num2 is greater')'''
'''num1=int(input("enter num1"))
num2=int(input("enter num2"))
print('num1 is greater'if(num1>num2)else 'num2 is greater')'''
a=50
b=10
c=-15
print('a'if a>b and a>c else 'b' if b>c else 'c')
