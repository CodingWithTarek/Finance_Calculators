# Getting this project code to GitHub.

import math  # Step 1: Import the math module

def get_user_choice():
    # Step 2: Get the user's choice for calculation
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    
    # Ensure the user enters a valid choice
    while True:
        user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
        if user_choice in ['investment', 'bond']:
            return user_choice
        else:
            print("Invalid input. Please enter 'investment' or 'bond'.")

def calculate_investment():
    # Step 3: Calculate investment based on user input
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate total amount based on the interest type
    if interest_type == 'simple':
        total_amount = amount * (1 + interest_rate * years)
    elif interest_type == 'compound':
        total_amount = amount * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return

    print(f"The total amount after {years} years of {interest_type} interest is: {total_amount:.2f}")

def calculate_bond():
    # Step 4: Calculate bond repayment based on user input
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate: ")) / 100
    months = int(input("Enter the number of months to repay the bond: "))

    # Calculate monthly interest rate and bond repayment
    monthly_interest_rate = interest_rate / 12
    bond_repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    print(f"The monthly bond repayment will be: {bond_repayment:.2f}")

def main():
    # Step 5: Main program logic
    choice = get_user_choice()

    if choice == 'investment':
        calculate_investment()
    elif choice == 'bond':
        calculate_bond()

if __name__ == "__main__":
    main()


