# Isiah Brown
# 11/10/2026
# Using floats to disperse change to simulate a customer using a self-checkout machine

import random

def disperse_change(change):
    
    if change == 0:
        print("No change due")
        
    # Calculate the amount of each coin need
    num_dollars = change // 100
    change = change - (num_dollars * 100)
    
    num_quarters = change // 25
    change = change - (num_quarters * 25)
    
    nums_dimes = change // 10
    change = change - (nums_dimes * 10)
    
    nums_nickels =  change // 5
    change = change - (nums_nickels * 5)
    
    nums_pennies = change // 1
    
    # Display coins owed
    
    if num_dollars > 0:
        print(num_dollars, end='')
        if num_dollars == 1:
            print(" Dollar")
        else:
            print(" Dollars")
            
            
    if num_quarters > 0:
        print(num_quarters, end='')
        if num_quarters == 1:
            print(" Quarters")
        else:
            print(" Quarters")
            
    if nums_dimes > 0:
        print(nums_dimes, end='')
        if nums_dimes == 1:
            print(" Dime")
        else:
            print(" DImess")
            
    if nums_nickels > 0:
        print(nums_nickels, end='')
        if nums_nickels == 1:
            print(" Nickel")
        else:
            print(" Nickels")
            
    if nums_pennies > 0:
        print(nums_pennies, end='')
        if nums_pennies == 1:
            print(" Penny")
        else:
            print(" Pennies")
            
def main():
    
    # Generate a random float with 2 decimal places as the amount the custer owes
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    
    # Display the amount owed
    print(f"You owe ${amount_owed:.2f}")
    
    # Prompt user to Enter a float as the cash they will put into the chackout machine
    amount = float(input("Enter the amount of money as a float: "))
    
    # Calculate change owed
    change_owed = amount - amount_owed
    
    # Display change owed
    print(f"Change is: ${change_owed:.2f}")
    
    #Convert change owed to an integer
    change_owed = round(change_owed * 100)
    
    # Call the function and pass change_owed as the parameter
    disperse_change(change_owed)
    
# Call main
main()
