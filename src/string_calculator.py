def add(string):
    if string == "":
        return 0
    else:
        if string.startswith("//"):
            string = string.replace("//", "")
            delimiter = string.split("\n")[0]
            string = string.strip(delimiter).strip("\n")
            string = string.replace(delimiter, ",")
        string = string.replace("\n", ",")
        numbers = string.split(",")
        return sum([int(number) for number in numbers])
