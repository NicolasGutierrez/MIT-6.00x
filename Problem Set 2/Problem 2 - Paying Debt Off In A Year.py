'''
Paying Debt Off In A Year:
    The goal of this code is to, given an starting balance and the anual interest rate,
    return the minimum monthly payment that you, as a debtor, should pay in order to finish
    paying your debt in a year. The method used is exhaustive search, which does its job
    but is not very efficient.
    
'''
def GetMinimumMonthlyPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12.0
    payment = 10        # initial guess
    remainingBalance = balance         #
    while remainingBalance > 0:
        remainingBalance = balance
        payment +=10
        for month in range(1,13):
            unpaidBalance = remainingBalance - payment
            remainingBalance = unpaidBalance * (1 + monthlyInterestRate)
    return 'Lowest Payment: ' + str(payment)
    
####################################################

print GetMinimumMonthlyPayment(3329,0.2)