'''numbers=[10,20,30,40,50]
square_numbers=[]
#for loop to square each elements
for num in numbers:
    square_numbers.append(num*num)
print(square_numbers)'''

#list comprehension
'''numbers=[10,20,30,40,50]
square_numbers=[num*num for num in numbers]
print(square_numbers)'''


#conditionals in list comprehension
#[expression for item in list if condition==true]
#filtering even numbers from a list
'''even_numbers=[num for num in range(1,10) if num%2 == 0]
print(even_numbers)'''


#finding vowels in word using list comprehension
'''word='varshini'
vowels='aeiou'
result=[char for char in word if char in vowels]

print(result)'''

#nested list comprehension
'''matrix[]=[[j for in range(5)]for i in range(3)]
print(matrix)
integer_input=list(map(int,input("enter integers separated by space:").split()))
float_input=list(map(float,input("enter float separated by space:").split()))
string_input=list(map(input("enter string separated by space:").split()))
print("integer_input:",integer input)
print("float_input:",float input)
print("string_input:",string input)'''


#storing  multiple data types in the same variable using a list
'''data=list(map(int,input("enter integers separated by space:").split()))
data.extend(list(map(float,input("enter float separated by space:").split())))
data.extend(input("enter string separated by space:").split())
print("data:",data)'''


# printing the how many times each input is repeat & display in dictionary
'''n=input('enter a string')
l=[]
l=n.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))'''

#displaying strings start with 'b'
'''my_dict={'apple':10,'banana':20,'angel':30,'balaji':40,'chennai':100,'zebra':120}
for key,value in my_dict.items():
    if key[0].lower()=='b':#for first letter,for second letter key[1]
        print(f"the value of '{key}' is {value}")'''
#1.python program to print sum of negative numbers,even numbers and positive odd numbers in list
#python program to print largest even and largest odd numbers in a list

'''list=[str(x) for x in input().split()]
list1=[]
for i in list:
    for j in range(len(i)):
        if(i[j]=='s'):
            list1.append(i)
print(list1) '''

#2
'''userinput=input('enter a string')
print([word for word in userinput.split() if 's' in word])'''
#3
'''m=input('enter string')
for i in m.split():
    if 's' in i.lower():
        print(i,end='')'''

'''n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
sum1=0
sum2=0
sum3=0
for j in b:
    if(j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    else:
        sum3=sum3+j
print("Sum of all positive even numbers:",sum1)#sum(i for i in values if i%2==0)
print("Sum of all positive odd numbers:",sum2)#sum(j for j in values if j%2!=0)
print("Sum of all negative numbers:",sum3)#sum(k for k in values if k<0)'''
#2
'''n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
d=[]
for i in b:#list comprehension
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1=count1+1
for j in d:
    count2=count2+1
print("Largest even number:",c[count1-1])#max(i for i in values if i%2==0)
print("Largest odd number",d[count2-1])#max(j for j in values if j%2!=0)'''
