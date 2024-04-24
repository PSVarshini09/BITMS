#write a python program to check the validity of passwords validation:
#at least 1 letter b/w [a-z] and letter between [A-Z]
#at least 1 number between[0-9]
#at least 1 character from[$#@]
#minimum length 6 characters
#maximum length 16 characters
import re
p=input('enter password')
x=True
if(len(p)<6 or len(p)>12):
    pass
elif not re.search('[a-z]',p):
    pass
elif not re.search('[A-Z]',p):
    pass
elif not re.search('[$#@]',p):
    pass
elif re.search('\s',p):
    pass
else:
    print('valid password')
    x=False
    pass
if x:
    print('not a valid password')

