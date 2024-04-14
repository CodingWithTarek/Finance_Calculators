import math  

def get_user_choice():
    # Display options to the user and get their choice
    print("Investment - to calculate the amount of interest you'll earn on your investment")
    print("Bond - to calculate the amount you'll have to pay on a home loan")
    
    # Ensure the user enters a valid choice
    while True:
        user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
        if user_choice in ['investment', 'bond']:
            return user_choice
        else:
            print("Invalid input. Please enter 'investment' or 'bond'.")

def calculate_investment():
    # Calculate investment based on user input
    principal = float(input("Enter the principal amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years for investment: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate total amount based on the interest type
    if interest_type == 'simple':
        total_amount = principal * (1 + annual_interest_rate * years)
    elif interest_type == 'compound':
        total_amount = principal * math.pow((1 + annual_interest_rate), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return

    print(f"The total amount after {years} years of {interest_type} interest is: {total_amount:.2f}")

def calculate_bond():
    # Calculate bond repayment based on user input
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months for bond repayment: "))

    # Calculate monthly interest rate and bond repayment
    monthly_interest_rate = annual_interest_rate / 12
    bond_repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    print(f"The monthly bond repayment will be: {bond_repayment:.2f}")

def main():
    # Main program logic
    user_choice = get_user_choice()

    if user_choice == 'investment':
        calculate_investment()
    elif user_choice == 'bond':
        calculate_bond()

if __name__ == "__main__":
    main()
