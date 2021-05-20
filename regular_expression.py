import re


if __name__ == '__main__':
    test = ["4123456789123456", "5123-4567-8912-3456", "61234-567-8912-3456", "4123356789123456",
            "5133-3367-8912-3456", "5123 - 3567 - 8912 - 3456"]

    for item in test:

        print("=====", item, "=====")
        # a string start from something
        if re.match("5133", item):
            print("A", "5133 start")

        pattern = re.compile("5133")
        if pattern.match(item):
            print("B", "5133 start")

        # there is something in a string
        if re.search("4123", item):
            print("C", "4123 exits")

        if re.match('.*4123', item):
            print("D", "4123 exits")

        occurrence = re.findall("3456", item)
        if occurrence:
            print("E", "3456 all place", occurrence)

        occurrence_ = re.findall("3456.", item)
        if occurrence_:
            print("F", "3456? all place", occurrence_)

        occurrence__ = re.findall("3456.?", item)
        if occurrence__:
            print("G", "3456(?) all place", occurrence__)

        array = re.findall(r"\d", item)
        # array = re.findall(r"\w", item)
        if array:
            print("H", array)

    for s in test:
        if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) \
                and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
            print("Valid")
        else:
            print("Invalid")
    print("-------------------------")
# ► It must start with a 4, 5 or 6.
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.

    for data in test:
        if not re.match(r"^[456]", data):
            print("Invalid A", data)
            continue

        pattern = re.compile(r"^[\d]{4}-[\d]{4}-[\d]{4}-[\d]{4}$")
        if not re.match(pattern, data):

            if re.match(r"[\d]{16}$", data):
                pass
            else:
                print("Invalid B", data)
                continue

        if re.search(r"([\d])\1\1\1", data.replace("-", "")):
            print("Invalid C", data)
            continue

        print("Valid", data)

