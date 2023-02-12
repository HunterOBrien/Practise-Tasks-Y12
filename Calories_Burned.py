
bikingTime = int(input("How long have you been biking for (hours):  "))
joggingTime = int(input("How long have you been jogging for (hours):  "))
swimmingTime = int(input("How long have you been swimming for (hours):  "))

bikingCalories = bikingTime * 200
swimmingCalories = swimmingTime * 275
joggingCalories = joggingTime * 475

bikingWeight = bikingCalories * 0.129714285714
swimmingWeight = bikingCalories * 0.129714285714
joggingWeight = bikingCalories * 0.129714285714

totalWeight = swimmingWeight + joggingWeight + bikingWeight

print(f"You have worked off {totalWeight:.2f}g")
