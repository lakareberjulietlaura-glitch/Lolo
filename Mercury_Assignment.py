def check_age(age):
    if age >= 16:
        return True
    else:
        return False

def get_fee(plan, age):    
    if plan == "Basic":
        if age >= 16:
            return 50000
        else:
            return -1
    elif plan == "Standard":
        if age >= 16:
            return 80000
        else:
            return -1
    elif plan == "Premium":
        if age >= 18:
            return 120000
        else:
            return -1
    else: 
        return -1

successful_registrations = 0 
total_monthly_fees = 0

while True:
    try:
        number_of_applicants = int(input("Enter the number of applicants: "))
        if number_of_applicants > 0:
            break
        else:
            print("Please enter a number > 0. ")
    except  ValueError:
        print("Invalid input. Please enter a whole number. ")

for i in range(number_of_applicants):
    print("\n--- Applicants", i + 1, "---")
    name = input("Enter applicant name: ")
    while True:
        try:
           age = int(input("Enter applicant age: "))
           break
        except ValueError:
           print("Invalid age. Please enter a whole number. ") 
    if not check_age(age):
       print("Registration rejected. ")
       print("Applicants must be at least 16 years old. ")
       continue
    plan = input("Enter membership plan (Basic, Standard, Premium): ")

    fee = get_fee(plan, age)
    if fee == -1:
        if plan == "Premium" and age < 18:
            print("Premium membership requires the applicant to be 18 or above. ")
        elif plan not in ["Basic", "Standard", "Premium"]: 
            print("Invalid membership plan. ")
        else:
            print("Registration rejected. ")
    else: 
        successful_registrations += 1
        total_monthly_fees += fee

        print("\n Registration successful! ")
        print("Name:", name)
        print("Age:", age)
        print("Membership plan:", plan)
        print("Monthly fee:", fee, "UGX")

print("Number of successful registration:", successful_registrations )
print("total monthly fees expected:", total_monthly_fees, "UGX")
                                                           