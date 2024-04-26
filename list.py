'''banana=[10,'varshini',25000.75,'z']
print(banana)
for i in banana:
    print(i,end=' ')
print()
pineapple=[10,'varshini',25000.75,'z']
print(pineapple)
print(pineapple==banana)'''


'''apple=[10,5,30]
print(apple)
print(apple[1])
print(apple[-3])
for i in apple:
    print(i,end=' ')
apple[-1]=100
print(apple)
apple[2]=(300,400)
print(apple)
print(apple[-1])
apple[1:4]=(-10,-20,-30)
print(apple)'''


'''college=[10,20,30,40,50,60,70,80,90,100]
print(college[1])
print(college[-1])
print(college[1:3])
print(college[1:7])
print(college[:])
print(college[-5:-1])
print(college[3:-1])
print(college[:-1])
print(college[0:])
print(college[0:4:3])
print(college[0:30:3])'''

'''varshini=[]
n=int(input('enter the list size'))
for i in range(0,n):
    ele=input('enter the elements')#int(input('enter element')) by default it take char
    varshini.append(ele)
print(varshini)'''


'''varshini=[10,20,30,40,50]
sanjana=[60,70,80,90,100]
vs=varshini+sanjana
print(vs)
print(type(varshini))
print(type(sanjana))
print(vs*2)# '*' is here repeatation
print(len(vs))
print(max(vs))
print(min(vs))'''


'''varshini=[10,20,30,40,50]
sum=0
for i in varshini:
    sum+=i
print(sum)'''


'''varshini=[10,25,37,40,57,65] #numbers which are ended up with 7
sum=0
for i in varshini:
    if i%10==7:
        print(i)'''

'''varshini=[10,20,30,40,50,30,50]
bitm=[]
for i in varshini:#i=10
    if i not in bitm:#i=10 not in bitm it moves to bitm
        bitm.append(i)#i=10
print(bitm)'''

'''a=[10,20,30,40,50]
b=[60,70,80,90,100,20]
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)'''              
        
    
        
      
    
       