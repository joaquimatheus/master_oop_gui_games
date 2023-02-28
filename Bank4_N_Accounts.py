accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
    global = accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('account', accountNumber)
    print('      Name', accountNamesList[accountNumber])
    print('      Balance:', accountBalancesList[accountNumber])
    print('      Password:', accountPasswordList[accountNumber])

def getBalance(accountNumber, password):
    global accountNamesList, accountBalanceList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalanceList, accountPasswordList
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountPasswordList[accountNumber]:
        print('Incorrect password')
        return None

    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + amountToDeposit
    return accountBalancesList[accountNumber]


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPasswordList[accountNumber]:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountsBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalancesList[accountNumber]

print("Joe's account is account number: ", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number: ", len(accountNamesList))
newAccount('Mary', 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdraw')
    print('Press s to show all accounts')
    print('Press q to quit!')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)

        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit')
        userAccountNumber = input('Please enter your account number: ')
