from Account import *

oJoesAccount = Account('Joe', 100, 'JoesPassword')
print('Created an account for Joe')

oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print('Created an account for Mary')

oJoesAccount.show()
oMarysAccount.show()
print()

print('Calling methods of the two accounts...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

oJoesAccount.show()
oMarysAccount.show()

print()
userName = input('What is the name for the newe user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)

oNewAccount.show()

oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)

oNewAccount.show()
