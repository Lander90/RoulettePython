import random
#Functions-------------------
 
#Definitions-----------------
money = 1000
alwaysTrue = True
colors = ['Red', 'Black']
numbers = random.randint(1,36)
highLow = ''
output = ''
bet = ['', '', 0]
parity = ''
win = 0
#Code------------------------
while alwaysTrue == True:
    if numbers % 2 == 0:
        parity = 'Even'
    elif numbers % 2 != 0:
        parity = 'Odd'
    if numbers > 18.5:
        highLow = 'High'
    elif numbers < 18.5:
        highLow = 'Low'
while alwaysTrue == True:
    print(parity+' ('+str(numbers)+')'+' and '+highLow)
    bet[0] = input("High (19-36) or Low (1-18): ")
    bet[1] = input("Guess Odds or Evens: ")
    bet[2] = input("How much would you like to bet? $")
    if bet[0] == 'High' or 'high' or 'Low' or 'low':
        break
    if bet[1] == 'Odds' or 'odds' or 'Evens' or 'evens':
        break
    if type(bet[2]) is int and bet[2]<= money:
        break

if bet[0] == highLow:
    win = bet[2]
    money = money + win
if bet[0] != highLow:
    win = -1*bet[2]
    money = money + win
