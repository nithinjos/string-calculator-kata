def replace_delimiters(string):
    """ Replace delimiters in the string with commas """
    string = string.replace("//", "")
    delimiter_conf = string.split("\n")[0]
    string = string.strip(delimiter_conf).strip("\n")
    delimiter = delimiter_conf.strip("[]")
    if "[" in delimiter:
        delimiters = delimiter.split("][")
        for each_delimeter in delimiters:
            string = string.replace(each_delimeter, ",")
    else:
        string = string.replace(delimiter, ",")
    return string


def get_numbers(string):
    """ Get numbers from the string """
    if string.startswith("//"):
        string = replace_delimiters(string)
    string = string.replace("\n", ",")
    return string.split(",")


def add(string):
    """ Add numbers in the string """
    if string == "":
        return 0
    else:
        numbers = get_numbers(string)
        negatives = [number for number in numbers if int(number) < 0]
        if negatives:
            raise ValueError(
                f"negative numbers not allowed: {', '.join(negatives)}")
        return sum([int(number) for number in numbers if int(number) <= 1000])
