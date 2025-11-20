# Ask the user for the distance they want to travel
distance = float(input("How far do you want to travel (in miles)? "))

# Check conditions and give suggestions
if distance < 3:
    print("You should ride a Bicycle.")
elif distance < 300:
    print("You should ride a Motor-Cycle.")
else:
    print("You should drive a Super-Car.")
