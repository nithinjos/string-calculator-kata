def add(string):
    if string == "":
        return 0
    else:
        numbers = string.split(",")
        return sum([int(number) for number in numbers])
