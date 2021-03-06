'''
Paying Debt Off In A Year:
    The goal of this code is to, given an starting balance and the anual interest rate,
    return the minimum monthly payment that you, as a debtor, should pay in order to finish
    paying your debt in a year. The method used is exhaustive search, which does its job
    but is not very efficient.
'''
import time
start_time = time.clock()           # start counting time

balance = 6.413E7                   # given starting balance
annualInterestRate = 0.2            # given annual interest rate
monthlyInterestRate = annualInterestRate/12.0
payment = 10                        # initial guess
remainingBalance = balance
while remainingBalance > 0:
    remainingBalance = balance
    payment +=10
    for month in range(1,13):
        unpaidBalance = remainingBalance - payment
        remainingBalance = unpaidBalance * (1 + monthlyInterestRate)
print 'Lowest Payment:', str(payment)
print '----------------'
print 'Calculation took:', str(time.clock() - start_time), 'seconds.'