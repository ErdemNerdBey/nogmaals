# name of student: Erdem
# number of student: 99065788
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # need to be payed
payed = int(float(input('Payed amount: ')) * 100) # payed money
change = payed - toPay # cange

if change > 0: # if cange is bigger than
  coinValue = 500 # = than the coin value is 50
  
  while change > 0 and coinValue > 0: # while change is bigger than 0 and coin value is bigger than 0
    nrCoins = change // coinValue # nr coins are change / coinvalue

    if nrCoins > 0: # if nr coins are bigger than 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # berekening'
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #howmuch coins he wants
      change -= nrCoinsReturned * coinValue # overig

# comment on code below: change in coins
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # overgebleven
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')