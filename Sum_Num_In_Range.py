
def list_creator():
    firstnum = int(input("Give Your First Number In Range: "))
    secondnum = int(input("Give Your Last Number In Range: "))
    num_list = []

    num_list.append(firstnum)

    while firstnum + 1 < secondnum:
        firstnum = firstnum + 1
        num_list.append(firstnum)

    num_list.append(secondnum)
    print(f"your range is: {num_list}")
    print(f"Your sum is: {sum(num_list)}")


print(list_creator())


