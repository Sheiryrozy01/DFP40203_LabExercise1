#MOHAMMAD SHEIRY ROZY
#20DDT19F1056
#Lab Exercise 1
#Sir Azlan
#QUESTION 1
x=1
for x in range(11):
    number=x*x
    print ("The square of",x,"=",number)

#MOHAMMAD SHEIRY ROZY
#Question 1b
#Lab exercise
#sum()
maximum =10
total = 0

for number in range(2, maximum + 1, 2):
    total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

#MOHAMMAD SHEIRY ROZY
#Question 2
#Lab exercise

name = input('Please enter you name:')
password = input('Please enter you Password:')
x = True
while x:
    if len(password)<5:
        break
    elif not re.search("[a-z]",p):
       break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Your password need to contain at least 5 characters")

#MOHAMMAD SHEIRY ROZY
#Question 3
#Lab exercise

carPrice=103300
downpayment=carPrice*0.1
downpaymentPay=int(input("Please enter your downpayment :"))#string
if downpayment<downpaymentPay:
    print("you not eligible for the bank loan")
else:
    print("eligible for bank loan")
    loanPeriod=float(input("Please enter your loan period in years :"))#string
    loanAmount=carPrice-downpaymentPay
    totalInterest=0.027*loanAmount*loanPeriod
    loanPeriodMonth=loanPeriod*12
    monthlyinstallment=round(((loanAmount+totalInterest)/loanPeriodMonth),2)

    print('You need to pay Rm',monthlyinstallment,'as your montly installment')














