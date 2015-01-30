'''
Paying Debt Off - Bisection Search:
    Given an initial balance and an annual interest rate, this program will use bisection search
    to find the minimum monthly payment necessary to pay off your debt after one year. This
    guessing method is much more efficient than the exhaustive search used in problem 2.
'''
import time
start_time = time.clock()           # start counting time

balance = 6.413E7                   # given starting balance
annualInterestRate = 0.2            # given annual interest rate
monthlyInterestRate = annualInterestRate/12.0         
lowerBound = balance/12                                     # lowest guess for the monthly payment
upperBound = (balance*(1+monthlyInterestRate)**12 )/12.0    # highest guess for the monthly payment
epsilon = 0.01
payment = (upperBound +lowerBound)/2.0          # first guess for the monthly payment
remainingBalance = balance                         
while abs(remainingBalance) >= epsilon:        # loops while -0.01 < balance < 0.01
    remainingBalance = balance                 # remaining balance is reset before trying next guess
    for month in range(1,13):
        unpaidBalance = remainingBalance - payment
        remainingBalance = unpaidBalance * (1 + monthlyInterestRate)
    if remainingBalance < 0:      # the guess was too high; therefore, this code is reducing the upper bound
        upperBound = payment            
    else:                         # the guess was too low; therefore, this code is augmenting the lower bound
        lowerBound = payment
    payment = (upperBound+lowerBound)/2.0
print 'Lowest Payment:', str(round(payment, 2))
print '----------------'
print 'Calculation took:', str(time.clock() - start_time), 'secconds.'