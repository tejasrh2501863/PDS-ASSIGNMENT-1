#6.A company needs a program that reads employee names and their basic salary.The program should: Calculate total salary including HRA (20%) and DA (10%).Stop taking input when the user types "stop". Display each employee’s total salary at the end.


print("Enter employee details. Type 'stop' to finish.\n")

while True:
    name = input("Enter employee name: ")

    if name.lower() == "stop":
        break

    basic = float(input("Enter basic salary: "))

    # Salary calculations
    hra = 0.20 * basic   # 20%
    da  = 0.10 * basic   # 10%
    total = basic + hra + da

    # Store in list
    employees.append((name, total))

    print("Salary added!\n")

# ----- Final Output -----
print("\n----- EMPLOYEE TOTAL SALARY REPORT -----")
for name, total in employees:
    print(f"Employee: {name} | Total Salary: ₹{total:.2f}")

