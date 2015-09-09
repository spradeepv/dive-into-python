balance = int(raw_input())
annualInterestRate = float(raw_input())

total_paid = 0
fixed_monthly_payment = 10
temp_balance = balance
while temp_balance > 0:
    temp_balance = balance
    for m in range(1, 13):
        monthly_interest_rate = annualInterestRate/12.0
        unpaid_balance = temp_balance - fixed_monthly_payment
        temp_balance = unpaid_balance + monthly_interest_rate * unpaid_balance
    print temp_balance, fixed_monthly_payment
    fixed_monthly_payment += 10
print temp_balance, fixed_monthly_payment
print "Total paid:", round(total_paid, 2)
print "Remaining balance:", round(balance, 2)
