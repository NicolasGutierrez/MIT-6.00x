# begin counting time until calculation ends
import time
start_time = time.clock()       
# given variables
balance = 6.413E7      
annualInterestRate = 0.2
# derived variables
monthlyInterestRate = annualInterestRate/12.0         
lowerBound = balance/12                                     # lowest guess for the monthly payment
upperBound = (balance*(1+monthlyInterestRate)**12 )/12.0    # highest guess for the monthly payment
epsilon = 0.01
payment = (upperBound +lowerBound)/2.0                      # first guess for the monthly payment
remainingBalance = balance                                  # new variable defined for convenience
while abs(remainingBalance) >= epsilon:       # loop while -0.01 > balance > 0.01
    remainingBalance = balance                              # remaining balance is reset to start trying the next guess
    for month in range(1,13):
        unpaidBalance = remainingBalance - payment
        remainingBalance = unpaidBalance * (1 + monthlyInterestRate)
    if remainingBalance < 0:      # the guess was too high; therefore, this code is reducing the upper bound
        upperBound = payment            
    else:                         # the guess was too low; therefore, this code is augmenting the lower bound
        lowerBound = payment
    payment = (upperBound+lowerBound)/2.0
print 'Lowest Payment: ' + str(round(payment, 2))
print time.clock() - start_time, "secconds"