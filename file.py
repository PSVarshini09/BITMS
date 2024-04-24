#slicing
'''a='varshini'
print(a[:])
print(a[2:])
print(a[::-1])
print(a[-5:-1])'''

#right to left after three characters in reverse order
'''a='varshini'
print(a[::-3])'''

'''name='varshini'
print(name)
print(name[::3])
print(name[::-3])for i in range(0,len(name)):
    if i%3==0 and i!=0:
        print('-',end='')
    else:
        print(name[i],end='')
sep='-'.join(name[::2])
print(sep)'''
        
#example1
'''fileptr=open("varshini.txt","r")
if fileptr:
    print('opened successfully')
fileptr.close()'''

#open and write,append of a file
'''fileptr=open("varshini.txt","a")
fileptr.write("always crispy")
print(fileptr)
if fileptr:
    print("always crispy")
fileptr.close()'''


#open and read a file
'''fileptr=open("varshini.txt","r")
content=fileptr.read()
print(content)
fileptr.close()'''
        
