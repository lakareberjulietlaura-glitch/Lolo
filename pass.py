marks =[45, 67, 89, 34, 76, 90, 55, 43, 78, 82]
#marks = []

def pass_rate(marks, threshold=50):
    if len(marks) == 0:
        return 0
    passed = 0
    for m in marks:
        if m >= threshold:
            passed += 1
    return (passed / len(marks)) * 100

print("Pass rate:", pass_rate(marks))
print("Distinction %:", pass_rate(marks, 80))