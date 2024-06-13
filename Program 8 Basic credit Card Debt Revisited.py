#Program 8 Basic: Credit Card Debt Revisted
#This program uses Recursion to calculate how many months it will take you to pay off your debt
#Daniel Jaffe
#Date Modified 4/1/24


#A subroutine to calculate how many months it takes to pay off your debt
def Month_pay_credit_card(debt,interest_rate,monthly_payment,month):
    debt = debt*(1+interest_rate/12)
    if debt >0:
        return Month_pay_credit_card(debt-monthly_payment,interest_rate,monthly_payment,month+1)
    else:
        return month
    


#Main program
debt = int(input("Give me amount of debt: "))
interest_rate = float(input("Input a interest rates in a percent: "))
interest_rate = interest_rate/100
monthly_payment = int(input("Input a Monthly Payment: "))
month = 1
month_to_pay_debt = Month_pay_credit_card(debt,interest_rate,monthly_payment,month)
print("It will take {} months to pay off your debt.". format(month_to_pay_debt))