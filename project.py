'''email='varshiniyadav319@gmail.com'
password='123456'
otp=2547
uemail=input('enter email')
upassword=input('enter password')
uotp=int(input('enter otp'))
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    if uemail==email and upassword==password and uotp==otp:
        choice = input("Enter your choice: ")
    else:
        print('invalid details')
    

    if choice == '5':
        print("Exiting program.")
        break

    if choice in choices:
        if choice == '1' or choice == '2':
            amount = float(input("Enter amount: "))
            choices[choice](account, amount)
        else:
            print(choices[choice](account))
    else:
        print("Invalid choice. Please try again.")'''


'''email=['varshiniyadav319@gmail.com','abc@gmail.com','efg@gmail.com']
password=['123456','234567','345678']
otp=[2547,3456,9876]
uemail=input('enter email')
upassword=input('enter password')
uotp=int(input('enter otp'))
for i in range(0,len(email)):
    if email[i]==uemail:
        print('valid email')
    else:
        print('invalid')
        break
for i in range(0,len(password)):
    if password[i]==upassword:
        print('valid')
    else:
        print('invalid')
        break
for i in range(0,len(otp)):
    if otp[i]==uotp:
        print('valid')
    else:
        print('invalid')
    break
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while email[i]==uemail and password[i]==upassword and otp[i]==uotp:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    
    choice=input('enter your choice')
    if choice == '5':
        print("Exiting program.")
        break
    if choice in choices:
        if choice == '1' or choice == '2':
            amount = float(input("Enter amount: "))
            choices[choice](account, amount)
        else:
            print(choices[choice](account))                
    else:
        print("Invalid choice. Please try again.")'''
    
        
'''email=["abc@gmail.com","def@gmail.com","ijk@gmail.com"]
password=[12345678,12345,98765]
uemail=str(input("Enter email"))
upaw=int(input("Enter password"))
for i in range(0,len(email)):
    if email[i]==uemail:
        if password[i]==upaw:
            print("Already registered")
            break
else:
    print("Register first")
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while  email[i]==uemail and password[i]==upaw:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program.")
        break

    if choice in choices:
        if choice == '1' or choice == '2':
            amount = float(input("Enter amount: "))
            choices[choice](account, amount)
        else:
            print(choices[choice](account))
    else:
        print("Invalid choice. Please try again.")'''

#writing output to a file and creating
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
        
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")
       

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    str1="\n".join([str(i) for i in account['transactions']])
    try:
        a=open("trans2.txt","x")
        a.write("Initial Balance: ")
        a.write(str(bal))
        a.write("\n")
        a.write(str1)
        a.write("\n")
        a.write('Remaining Balance: $')
        a.write(str(account['balance']))
        a.write("\n")
        a.close()
        return account['transactions']
    except FileExistsError:
        a=open("trans2.txt","w")
        a.write("Initial Balance: ")
        a.write(str(bal))
        a.write("\n")
        a.write(str1)
        a.write("\n")
        a.write('Remaining Balance: $')
        a.write(str(account['balance']))
        a.write("\n")
        a.close()
        return account['transactions']
        

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}
bal='$'+str(account['balance'])
# Dictionary to map user choices to functions
m=0
e=input("enter your email:")
p=input("enter your password:")
p1="0123"
e1="zealgaming4@gmail.com"
if(e==e1) and (p==p1):
    choices = {
        '1': deposit,
        '2': withdraw,
        '3': get_balance,
        '4': get_transaction_history
}

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        if choice in choices:
            if choice == '1':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)
            
            elif choice == '2':
                
               
                m=m+1
                if m>5:
                    print("withdrawing limit reached")
                else:
                    amount = float(input("Enter amount: "))
                    choices[choice](account, amount)
        
            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid credentials")
                
                
            
            
        
                
    
           
     
            
        
    
    

    