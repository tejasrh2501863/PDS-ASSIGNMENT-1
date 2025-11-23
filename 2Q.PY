#2.An App for Mobile hosting provider charges- $0.51 per hour how much does it cost to operator per day, per week, per month? how many days can i operate one server with$918?
cost_per_hour = 0.51

# Calculations
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

# Money available
balance = 918
days_you_can_operate = balance / cost_per_day

# Output results
print("Cost to operate per day: $", round(cost_per_day, 2))
print("Cost to operate per week: $", round(cost_per_week, 2))
print("Cost to operate per month: $", round(cost_per_month, 2))
print("Days you can operate one server with $918:", round(days_you_can_operate, 2))


