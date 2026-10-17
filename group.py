
def safe_int(prompt): 
    while True: 
        try: 
            number = int(input(prompt))
            return number 
        except ValueError: print("Invalid input. Please enter an integer.") 
        
        def grade(mark): 
            if mark >= 50: 
                return "Pass" 
            else: return "Fail" # 
             
        while True:
            number_of_students = safe_int("How many students do you want to process? ") 
            if number_of_students > 0: 
                break 
            else: 
                print("Please enter a number greater than 0.")
                
names = [] 
attendance = []
marks = []  
for i in range(number_of_students): 
    print("\nStudent", i + 1) 
    name = input("Enter student name: ")
    names.append(name) 
    while True: 
        attend = input("Enter attendance (P for Present, A for Absent): ").upper() 
        if attend == "P" or attend == "A": 
            attendance.append(attend) 
            break 
        else: 
            print("Invalid attendance. Please enter P or A.") 
            while True: 
                mark = safe_int("Enter quiz mark (0-100): ") 
                if mark >= 0 and mark <= 100: 
                    marks.append(mark) 
                    break 
                else:
                    print("Invalid mark. Enter a number between 0 and 100.") 
                    print("\n========== SESSION SUMMARY ==========") 
passed = 0 
failed = 0 
present = 0 
absent = 0 
for i in range(number_of_students): 
    student_grade = grade(marks[i]) 
    print( "Name:", names[i], "| Attendance:", attendance[i], "| Mark:", marks[i], "| Grade:", student_grade ) 

    if attendance[i] == "P": 
     present += 1
    else: absent += 1 
if student_grade == "Pass": passed += 1 
else:
    failed += 1
    average_mark = sum(marks) / len(marks) 
    print("\n---------- Statistics ----------") 
    print("Number Present:", present) 
    print("Number Absent:", absent) 
    print("Average Mark:", round(average_mark, 2))    