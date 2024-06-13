def monthlycalc(balances,interestrate,monthlypayment,totalpayment,month):
    while balances >=0:
        month += 1
        interestrate = balances * (interestrate/12)
        balances += interestrate
        balances -= monthlypayment
        totalpayment += monthlypayment
        print (balances)
    return"It takes " + str(month) + " month to get to a balance of zero or less"

balance = (float(input("Outstanding balance on your credit card: ")))
interest_rate = float(input("Annual interest rate (as a decimal): "))
monthly_payment = float(input("Minimum monthly payment (as a decimal): "))
total_amount_paid = 0
months = 0

balancezero=monthlycalc(balance,interest_rate,monthly_payment,total_amount_paid,months)
print(balancezero)
