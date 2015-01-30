'''
Paying The Minimum:
    Given an initial balance, an annual interest rate and a minimum monthly payment rate,
    this code will return the remaining balance month by month for twelve months, in the case
    assuming that you pay the minimum possible payment each month.
'''
import time
start_time = time.clock()           # start counting time

balance = 16374                     # given starting balance
annualInterestRate = 0.2            # given annual interest rate
monthlyPaymentRate = 0.04           # given minimum monthly payment
month = 1
while month <= 12:
    print 'Month: ' + str(month)
    monthlyPay = round(balance * monthlyPaymentRate, 2)
    unpaidBalance = round((balance - monthlyPay), 2)
    balance = round(unpaidBalance * (1 + annualInterestRate/12.0), 2)
    month += 1
    print 'Minimum Monthly Payment: ' + str(monthlyPay)
    print'Remaining balance: ' + str(balance)
print '----------------'
print 'Calculation took:', time.clock() - start_time, 'seconds.'