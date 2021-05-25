import re


def rangeOfNBitsSignMagnitude(N):
    # return smallest number,largest number,total number
    return - (2 ** (N - 1) - 1), 2 ** (N - 1) - 1, 2 ** N - 1


def rangeOfNBitsTwoCompliments(N):
    # return smallest number,largest number,total number
    return - (2 ** (N - 1)), 2 ** (N - 1) - 1, 2 ** N


def bitToDecimalTwoCompliments(x):
    print(x)
    print("Number","\t", "2^N","\t", "Place Value\t", "Cumulated Value")
    x = str(x)
    if re.findall("[0-1]*", x):
        total = 0
        for idx, char in enumerate(x[::-1]):
            if char == '1':
                total += (2 ** idx)
            print(char, "\t\t", idx, "\t\t", 2 ** idx, "\t\t\t\t", total)
        return "Number in Decimal : " + str(total)
    else:
        return None


print(bitToDecimalTwoCompliments("00110"))
