employees = []   # To store employee records as (name, total_salary)

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
