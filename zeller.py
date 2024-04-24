'''class mango:
    def __init__(self):
        print('this is what')
    def varshini(self):
        print('this is without para')
    def abc(self,a,b):
        print(a+b,'this is with para')
    def magicalprime(self):
        a=int(input('enter a number'))
        rev=0
        if a%2==0:
            print('prime number')
        else:
            print('not prime number')
        
    def neon(self,a):
        def is_neon_number(n):
    square = n * n
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n

# Example usage:
for num in range(1, 101):
    if is_neon_number(num):
        print(num, "is a neon number.")
man=mango()
man.varshini()
man.abc(10,20.5)
man.magicalprime()
man.neon(7)'''



'''class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty, amount):
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

# Example usage:
account = BankAccount(1000)
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)
print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())'''

'''def switch(h) :

    return {

        0 : "Saturday",

        1 : "Sunday",

        2 : "Monday",

        3 : "Tuesday",

        4 : "Wednesday",

        5 : "Thursday",

        6 : "Friday",

    }[h]
 
def Zellercongruence(day, month, year) :

    if (month == 1) :

        month = 13

        year = year - 1
 

    if (month == 2) :

        month = 14

        year = year - 1

    q = day

    m = month

    k = year % 100;

    j = year // 100;
    if year in range(1900,9999):
        if month in range(1,12):
            h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
            h = h % 7
            print(switch(h))
        else:
            print('invalid month')
    else:
        print('invalid year')
day=int(input('enter day'))
month=int(input('enter month'))
year=int(input('enter year'))
#if (month<0 or month>12) or (day<0 or day>31) or (year<1900 or year>9999):
Zellercongruence(day,month,year)'''

'''d=int(input("Enter The Date : ")) 
if(d>0 and d<=31):
    m=int(input("Enter The Month : "))
    if(m>0 and m<12):
        if(((d<=31) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)) or((d<=30) and(m==4 or m== 6 or m==9 or m==11)) or ((d<=29) and (m==2))):
            y=int(input("Enter The Year : "))
            if (y>1900 and y<9999):
                c=y//100
                D=y%100
                if m>2:
                    m-=2
                else:
                    m+=1

                f=d+((13*m-1)/5)+D+D/4+(c/4)-2*c
                fres=int(f%7)
                day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
                print(day[fres])
            else:
                print("Incorrect Year")
        else:
            print("Invalid Date")
    else:
        print("Incorrect Month")
else:
    print("Incorrect Date")'''



