resultsList = []
namesList = []


while input("Enter 'x' if finished: ") != "x":
    studentName = input("What is your student's name: ")
    studentResult = int(input("What is your student's mark out of 100: "))
    namesList.append(studentName)
    resultsList.append(studentResult)

topMarkIndex = resultsList.index(max(resultsList))
print(f" The best result was {max(resultsList)} by {namesList[topMarkIndex]} with an average score of {sum(resultsList) / len(resultsList)}")


while len(namesList) > 0:
    print(namesList.pop())
    print(f"got a score of {resultsList.pop()}")

    if resultsList.pop() > 89:
        print("Which gives them an A+")

    elif resultsList.pop() > 84:
        print("Which gives them an A")

    elif resultsList.pop() > 79:
        print("Which gives them an A-")

    elif resultsList.pop() > 74:
        print("Which gives them an B+")

    elif resultsList.pop() > 69:
        print("Which gives them an B")

    elif resultsList.pop() > 64:
        print("Which gives them an B-")

    elif resultsList.pop() > 59:
        print("Which gives them an C+")

    elif resultsList.pop() > 54:
        print("Which gives them an C")

    elif resultsList.pop() > 49:
        print("Which gives them an C-")

    elif resultsList.pop() > 44:
        print("Which gives them an D")

    elif resultsList.pop() > 39:
        print("Which gives them an E")
