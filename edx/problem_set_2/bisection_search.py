balance = int(raw_input())
annualInterestRate = float(raw_input())

lo_monthly_payment = balance/12.0
hi_monthly_payment = (balance * (1 + (annualInterestRate/12.0))**12)/12.0
fixed_monthly_payment = (hi_monthly_payment + lo_monthly_payment) / 2
temp_balance = balance

def pay(monthly_payment, my_balance):
    for m in range(1, 13):
        my_balance = my_balance - monthly_payment
        my_balance = my_balance + ((annualInterestRate/12.0) * my_balance)
        if my_balance <= 0 :
            break
    return round(my_balance, 2)


while abs(temp_balance) != 0.00:
    temp_balance = pay(fixed_monthly_payment, balance)
    if temp_balance > 0:
        lo_monthly_payment = fixed_monthly_payment
    elif temp_balance < 0:
        hi_monthly_payment = fixed_monthly_payment
    fixed_monthly_payment = (lo_monthly_payment + hi_monthly_payment) / 2

print "Lowest Payment:", round(fixed_monthly_payment, 2)
