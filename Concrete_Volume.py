stopper = ""
buildingType = ""

while stopper != "x":
    buildingType1 = input("Enter '1' for Residential or '2' for Commercial building: ")
    if buildingType1 == "x":
        quit()
    else:
        buildingType = buildingType1
    buildingLen = int(input("What is the length of your building (m) : "))
    buildingWidth = int(input("What is the width of your building (m) : "))
    buildingDepth = int
    buildingVol = int

    if buildingType == 1:
        buildingDepth = 0.25
    else:
        buildingDepth = 0.5

    buildingVol = buildingDepth * buildingWidth * buildingLen
    print(f"The volume of concrete required for a slab with a length of {buildingLen}, and a width of {buildingWidth}, and a volume of {buildingDepth} is {buildingVol}m ")


