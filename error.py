try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Result:", a/b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")        