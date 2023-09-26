# DISCOUNT CALCULATOR

total_cost = int(input("Enter the total cost of your shopping cart : "))
name = str(input("What is your name? "))

if total_cost >= 50:
    Amount_payable = ((total_cost) * 0.1)
    print("--------EXPENSE---------")
    print(name)
    print("Amount Payable : " +str(Amount_payable))
    print("-----THANK YOU-----")

else:
    print("--------EXPENSE---------")
    print(name)
    print("Amount Payable : " +str(total_cost))
    print("-----THANK YOU-----")

    
