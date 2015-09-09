balance = int(raw_input())
annualInterestRate = float(raw_input())
monthlyPaymentRate = float(raw_input())

total_paid = 0
for m in range(1, 13):
    print "Month:", m
    minimum_monthly_payment = monthlyPaymentRate * balance
    print "Minimum monthly payment:", round(minimum_monthly_payment, 2)
    unpaid_balance = balance - minimum_monthly_payment
    balance = unpaid_balance + (annualInterestRate/12) * unpaid_balance
    print "Remaining balance:", round(balance, 2)
    total_paid += minimum_monthly_payment
print "Total paid:", round(total_paid, 2)
print "Remaining balance:", round(balance, 2)
