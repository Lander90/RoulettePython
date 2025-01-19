import random
#Functions-------------------
def numCheck():
    if numbers % 2 == 0:
        parity = 'Even'
    elif numbers % 2 != 0:
        parity = 'Odd'
    if numbers > 18.5:
        highLow = 'High'
    elif numbers < 18.5:
        highLow = 'Low'
        
def spinWheel():
    print(parity+' ('+str(numbers)+')'+' and '+highLow)
#Definitions-----------------
money = 1000
always1 = 1
colors = ['Red', 'Black']
numbers = random.randint(1,36)
highLow = ''
output = ''
bet = ['', '', 0]
parity = ''
win = 0
#Code------------------------
while True:
    numCheck()
    print("\033[H\033[J", end="")
    print('Money: $' + str(money))
    bet[0] = input("High (19-36) or Low (1-18): ")
    bet[1] = input("Guess Odds or Evens: ")
    bet[2] = input("How much would you like to bet? $")
    if bet[0] == 'High' or 'high':
        bet[0] == 'Low'
    if bet[0] == 'Low' or 'low':
        bet[0] = 'Low'
    if bet[1] == 'Odds' or 'odds':
        bet[1] = 'Odd'
    if bet[1] == 'Evens' or 'evens':
        bet[1] = 'Even'
    if type(bet[2]) is int and bet[2]<= money:
        numCheck()
        break

if bet[0] == highLow:
    win = bet[2]
    money = money + win
if bet[0] != highLow:
    win = -1*bet[2]
    money = money + win
