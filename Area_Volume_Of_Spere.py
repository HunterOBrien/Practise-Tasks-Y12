radiusSphere = float(input("What is the radius of your sphere (cm): "))

areaSphere = 4 * 3.14 * pow(radiusSphere, 2)
volumeSphere = 4/3 * 3.14 * pow(radiusSphere, 3)

print(f"Area = {areaSphere:.2f}cm while volume = {volumeSphere:.2f}cm")
