def Add(numbers):
    if numbers == "":
        return 0
    splitted_numbers = numbers.replace("\n",",").split(",")
    print(splitted_numbers)
    x=0
    for i in splitted_numbers:
        x += int(i)
    return  x
