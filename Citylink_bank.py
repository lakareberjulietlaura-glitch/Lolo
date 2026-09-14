 #Name: LAKAREBER JULIET LAURA
 #REG NUMBER: S26B38-069
 #This program processes Citylink Mini_Bank customers and determines 
#whether they qualify for an account and have deposited the minimum amount.


def check_eligibility(age, account_type):
    """Check whether a customer is eligilible for the selected account."""
    if account_type == "S":
        return True
    elif account_type == "C":
        return True
    elif account_type == "T":
        if age <= 25:
            return True
        else:
            return False

def get_minimum_deposit(account_type):
    """Return the minimum deposit required for the account type."""
    if account_type == "S":
        return 50000
    elif account_type == "C":
        return 100000
    elif account_type == "T":
        return 20000
    else: 
        return 0

number_of_customers = int(input("How many customers?"))
accounts_opened = 0
total_deposited = 0

for customer in range(1, number_of_customers + 1):
    print(f"\n--- Customer{customer} ---")
    name = input("Name: ")
    age = int(input("Age: "))
    account_type = input("Account type (S/C/T): ").upper()

    if account_type not in ["S", "C", "T"]:
        print("Invalid account type. Please choose S, C or T. ")
    else:
        if check_eligibility(age, account_type):
            minimum_deposit = get_minimum_deposit(account_type)
            deposit = float(input("Initial deposit:"))
            if deposit >= minimum_deposit:
                accounts_opened += 1
                total_deposited += deposit
                print(f"Account opened successfully for {name}. "
                      f"Balance: {deposit: 0f} UGX"
                      )
            else: 
                if account_type == "S":
                   account_name = "Savings"
                elif account_type == "C":
                     account_name = "Current"
                else:
                     account_name = "Student"
                print(f"Deposit too low. Minimum for {account_name} "
                      f"is {get_minimum_deposit} UGX."
                      )
        else: 
            if account_type == "T" and age > 25:
                print("Sorry, Student accounts are only for age 25 or below."
                      )

print("\n===== SESSION SUMMARY =====")
print(f"Accounts opened: {accounts_opened}")
print(f"Total deposited: {total_deposited: 0f} UGX")                         