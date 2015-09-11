balance = int(raw_input())
annualInterestRate = float(raw_input())

total_paid = 0
fixed_monthly_payment = 0
temp_balance = balance
while temp_balance > 0:
    fixed_monthly_payment += 10
    temp_balance = balance
    for m in range(1, 13):
        monthly_interest_rate = annualInterestRate/12.0
        unpaid_balance = temp_balance - fixed_monthly_payment
        temp_balance = unpaid_balance + monthly_interest_rate * unpaid_balance

print "Lowest Payment:", fixed_monthly_payment
