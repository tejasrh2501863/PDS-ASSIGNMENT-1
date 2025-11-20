# Program to record 12 hourly speeds and analyze traffic flow

speeds = []

print("Enter the average speed for each of the 12 hours:")

# Reading 12 speed values
for i in range(1, 13):
    speed = float(input(f"Hour {i} speed: "))
    speeds.append(speed)

# Calculate average speed
avg_speed = sum(speeds) / 12

# Determine traffic flow condition
if avg_speed < 40:
    flow = "Slow"
elif avg_speed <= 80:
    flow = "Normal"
else:
    flow = "Fast"

# Output
print("\n----- TRAFFIC REPORT -----")
print("Average Speed:", round(avg_speed, 2))
print("Traffic Flow:", flow)
