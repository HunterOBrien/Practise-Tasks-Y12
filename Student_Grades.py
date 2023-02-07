resultsList = []
namesList = []
totalList = []


while input("Enter 'x' if finished: ") != "x":
    studentName = input("What is your student's name: ")
    studentResult = int(input("What is your student's mark out of 100: "))
    namesList.append(studentName)
    resultsList.append(studentResult)
    totalList.append(studentName)
    totalList.append(studentResult)


topMarkIndex = resultsList.index(max(resultsList))
print(f" The best result was {max(resultsList)} by {namesList[topMarkIndex]}")
