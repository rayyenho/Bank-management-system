from random import randint
import csv

try :
    with open('accounts.csv', 'x', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['No', 'Name', 'Type', 'Balance'])
        csvfile.close()
except:
    pass


class Account:

    #  The class constructor
    def __init__(self, name, accountNo, type, balance):
        self.__name = name
        self.__accountNo = accountNo
        self.__type = type
        self.__balance = balance

    #  Name setter
    def setName(self, name):
        self.__name = name

    #  Account number setter
    def setAccountNo(self, accountNo):
        self.__accountNo = accountNo

    #  Account type setter
    def setType(self, type):
        self.__type = type

    #  A method to deposit cash in the account
    def deposit(self, deposit ):
        self.__balance += deposit

    #  Name getter
    def getName(self):
        return self.__name

    #  Account number getter
    def getAccountNo(self):
        return self.__accountNo

    #  Account type getter
    def getType(self):
        return self.__type

    #  Account balance getter
    def getBalance(self):
        return self.__balance

    #  A method to withdraw cash from the account
    def withdraw(self, amount):
        if self.__balance - amount >= -1000:
            self.__balance -= amount
            print('Transaction proceeded successfully')
        else:
            print('Failed transaction, your balance cannot be less than -1000')

    #  Overriding __str__ so it would return the account info
    def __str__(self):
        return "Account number :"+str(self.__accountNo) + ' Full Name :' + self.__name + ' Type :' + self.__type + ' Balance : ' + str(self.__balance)



# A function that creates an account
def CreateAccount():
    print('Your are creating a new account')
    name = input('Enter your full name ')
    accountNo = SetAccountNo()
    while True :
        type = input('Select your account type: press "S" for savings account and "C" for current account').upper()
        if type == 'S':
            while True:
                deposit = int(input('Enter the amount you want to deposit'))
                if deposit >= 500:
                    break
                else:
                    print('To create a savings account you have to deposit an amount greater or equal to 500$')
            break
        elif type == 'C':
            while True:
                deposit = int(input('Enter the amount you want to deposit'))
                if deposit >= 200:
                    break
                else:
                    print('To create a current account you have to deposit an amount greater or equal to 200$')
            break
    
        else:
            print('Invalid choice')
    return Account(name, accountNo, type, deposit)


#  A function that checks that the account number is unique
def SetAccountNo():
    number = randint(10000000,99999999)
    with open('accounts.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for line in csv_reader:
            if line['No'] == number:
                number = randint(10000000,99999999)
                break
    csvfile.close()
    return number


#  A function to search for and display an account by the account number
def Display():
    global No
    No = input('Enter the number of the account you want to display')
    with open('accounts.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        exist =False
        for line in csv_reader:
            if line['No'] == No:
                exist = True
                break
        if exist==True:
            return "Account Number : {} Full Name : {} Type : {} Balance : {}".format(line['No'], line['Name'] ,line['Type'] ,line['Balance'])

        else:
            return 'The account you are searching for does not exist.'
    csvfile.close()


#  A function that creates the new updated account then deletes the old one
def Update(x):
    with open('accounts.csv', 'r+') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        csv_writer = csv.DictWriter(csvfile, ['No', 'Name', 'Type', 'Balance'])
        for line in csv_reader:
            if line['No'] == No:
                y = line['No'] + ',' + line['Name'] + ',' + line['Type'] + ',' +line['Balance']
                line['Name'] = input('Enter the new name')
                while True:
                    line['Type'] = input('Enter the new type').upper()
                    if line['Type'] == 'S' or line['Type'] == 'C':
                        break
                row = {'No': line['No'], 'Name': line['Name'], 'Type': line['Type'], 'Balance': line['Balance']}
                s = "Account Number : {} Full Name : {} Type : {} Balance : {}".format(line['No'], line['Name'] ,line['Type'] ,line['Balance'])
                csv_writer.writerow(row)
    Close(y)
    csvfile.close()
    print('Your account has been updated: ' + s)
    return s


#  A function that rewrites the accounts in the file except from the account the user wants to delete
def Close(account):
    with open('accounts.csv', "r") as csvfile:
        lines = csvfile.readlines()
    with open('accounts.csv', "w") as csvfile:
        for line in lines:
            if line.strip("\n") != account:
                csvfile.write(line)
    csvfile.close()


def Deposit(x):
    amount = input('Enter the amount you want to deposit: ')
    with open('accounts.csv', 'r+') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        csv_writer = csv.DictWriter(csvfile, ['No', 'Name', 'Type', 'Balance'])
        for line in csv_reader:
            if line['No'] == No:
                k = line['No'] + ',' + line['Name'] + ',' + line['Type'] + ',' + line['Balance']
                line['Balance'] = int(line['Balance']) + int(amount)
                row = {'No': line['No'], 'Name': line['Name'], 'Type': line['Type'], 'Balance': line['Balance']}
                s = line['No'] + ',' + line['Name'] + ',' + line['Type'] + ',' + str(line['Balance'])
                csv_writer.writerow(row)
    Close(k)
    print('Your new balance is: ', line['Balance'])
    csvfile.close()
    return s


def Withdraw(x):
    amount = input('Enter the amount you want to withdraw: ')
    valid = False
    with open('accounts.csv', 'r+') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        csv_writer = csv.DictWriter(csvfile, ['No', 'Name', 'Type', 'Balance'])
        for line in csv_reader:
            if line['No'] == No:
                if int(line['Balance']) - int(amount) >= -1000:
                    y = line['No'] + ',' + line['Name'] + ',' + line['Type'] + ',' + line['Balance']
                    valid = True
                    line['Balance'] = str(int(line['Balance']) - int(amount))
                    row = {'No': line['No'], 'Name': line['Name'], 'Type': line['Type'], 'Balance': line['Balance']}
                    s = line['No'] + ',' + line['Name'] + ',' + line['Type'] + ',' + line['Balance']
                    csv_writer.writerow(row)
                    print('Your new balance is: ', line['Balance'])

                elif int(line['Balance'])+1000 > 0:
                    print('The maximum withdraw amount available for this account is: ', int(line['Balance'])+1000)
                else:
                    print("The account has reached it's minimum balance, you cannot withdraw.")
    if valid:
        Close(y)
        return s
    else:
        return x
    csvfile.close()

# A function to display all accounts in the csv file
def DisplayAll():
    with open('accounts.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        m=0
        for line in csv_reader:
            if m==0:
                m+=1
                continue
            else:
                print("Account Number : {} Full Name : {} Type : {} Balance : {}".format(line[0], line[1] ,line[2] ,line[3]))
    csvfile.close()

def Sort():
    with open('accounts.csv', "r") as csvfile:
        lines = csvfile.readlines()
    with open('accounts.csv', "w") as csvfile:
        for line in lines:
            if line.strip("\n") != '':
                csvfile.write(line)
    csvfile.close()


print('Welcome to XXX bank')
while True:
    print('Press 1 to create an account. \nPress 2 to display an account information. \nPress 3 to display all accounts. \nPress 0 to exit.')
    operation = input()
    if operation == '1':
        a = CreateAccount()
        #  Adding the account to the file
        with open('accounts.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([a.getAccountNo(), a.getName(), a.getType(), a.getBalance()])
            csvfile.close()
        print('You have successfully created your account: ', a)

    elif operation == '2':
        x = Display()
        print(x)
        while  x != 'The account you are searching for does not exist.':
            print('Press 1 to withdraw cash.\nPress 2 to deposit cash.\nPress 3 to update the account\nPress 4 to close the account\nPress 0 to go back to the menu.')
            op = input()
            if op == '1':
                x = Withdraw(x)
                Sort()
            elif op == '2':
                x = Deposit(x)
                Sort()
            elif op == '3':
                x = Update(x)
                Sort()
            elif op == '4':
                Close(x)
                Sort()
                print('The account is permanently closed.')
                break
            elif op == '0':
                break

    elif operation == '3':
        DisplayAll()
    elif operation == '4':
        Update()
    elif operation == '0':
        break


