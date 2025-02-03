def get_numbers(string):
    if string.startswith("//"):
        string = string.replace("//", "")
        delimiter = string.split("\n")[0]
        string = string.strip(delimiter).strip("\n")
        string = string.replace(delimiter, ",")
    string = string.replace("\n", ",")
    return string.split(",")


def add(string):
    if string == "":
        return 0
    else:
        numbers = get_numbers(string)
        negatives = [number for number in numbers if int(number) < 0]
        if negatives:
            raise ValueError(
                f"negative numbers not allowed: {', '.join(negatives)}")
        return sum([int(number) for number in numbers])
