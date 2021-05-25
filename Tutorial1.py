import re
print("\033[96m",end="")
print("This a calculator that perform addition between two 8 bit floating point numbers.\n".upper())
print("\033[00m",end="")
# hex1 = "C0123456"
# hex2 = "81C564B7"

def isValid8BitFloatingPointNumber(num):
    if len(num) != 8:
        return False
    try:
        int(num, 16)
        return True
    except:
        return False


def askForValid8BitFloatingPointNumber(prompt):
    num = input(prompt)
    while not isValid8BitFloatingPointNumber(num):
        print("\033[91mInvalid 8-bit floating point number! Please give a valid 8-bit floating point number.\033[00m\n")
        num = input(prompt)
    return num


hex1 = askForValid8BitFloatingPointNumber("What is your first 8-bit floating point number? ")
hex2 = askForValid8BitFloatingPointNumber("What is your second 8-bit floating point number? ")

print(f"\nFirst Number : {hex1}")
print(f"Second Number: {hex2}")
num1 = int(hex1, 16)
num2 = int(hex2, 16)

bin1 = bin(num1)[2:].zfill(32)
bin2 = bin(num2)[2:].zfill(32)

# print(bin1[0],bin1[1:5],bin1[5:9],bin1[9:12],bin1[12:16],bin1[16:20],bin1[20:24],bin1[24:28],bin1[28:])
print("sign\texponent\tfraction")
print(bin1[0] + "\t\t" + bin1[1:9] + "\t" + bin1[9:])
print(bin2[0] + "\t\t" + bin2[1:9] + "\t" + bin2[9:])

if bin1[0] != bin2[0]:
    print("\n\033[91mThe sign of two numbers are different. This calculator cannot process subtraction.")
    quit()

exp1 = int(bin1[1:9], 2)
exp2 = int(bin2[1:9], 2)

man1 = bin1[9:]
man2 = bin2[9:]

print("\n1.	Extract exponent and fraction bits\n")
print(f"For First Number(N1)  : S = {bin1[0]} \tE = {exp1} \tF = .{man1}")
print(f"For Second Number(N2) : S = {bin2[0]} \tE = {exp2} \tF = .{man2}")

print("\n2.	Prepend leading 1 to form mantissa\n")
print(f"N1 : 1.{man1}")
print(f"N2 : 1.{man2}")

print("\n3.	Compare exponents\n")
diff = 0
exp = 0
if exp1 == exp2:
    print("The exponents are same. No shifting is required.")
    exp = exp1
elif exp1 < exp2:
    exp = exp2
    diff = -(exp1 - exp2)
    print(f"{exp1} - {exp2} = {exp1 - exp2}, so shift N1 right by {diff} bit")
else:
    exp = exp1
    diff = exp1 - exp2
    print(f"{exp1} - {exp2} = {exp1 - exp2}, so shift N2 right by {diff} bit")
print(f"E = {exp}")

print("\n4.	Shift smaller mantissa if necessary\n")
if exp1 == exp2:
    print("The exponents are same. No shifting is required.")
    man1 = "1." + man1
    man2 = "1." + man2
elif exp1 < exp2:
    newMan1 = "0." + ("1" + man1)[:-1 * diff].zfill(23)
    print(f"shift N1’s mantissa by {diff} bit: 1.{man1} >>> {newMan1}")
    man1 = newMan1
    man2 = "1." + man2
else:
    newMan2 = "0." + ("1" + man2)[:-1 * diff].zfill(23)
    print(f"shift N2’s mantissa by {diff} bit: 1.{man2} >>> {newMan2}")
    man1 = "1." + man1
    man2 = newMan2

print("\n5.	Add mantissas\n")
print("   " + man1)
print("+  " + man2)
F = bin(int(man1.replace(".", ""), 2) + int(man2.replace(".", ""), 2))[2:]
F = F[0:-23] + "." + F[-23:]
print(f"= {F}")

print("\n6.	Normalize mantissa and adjust exponent if necessary\n")
adjust = 0
if F.split(".")[0] == "1":
    print("No normalization of mantissa is required")
else:
    print(f"{F} = ", end="")
    part1 = F.split(".")[0]
    part2 = F.split(".")[1]
    F = part1[0:-1] + "." + part1[-1] + part2
    adjust = len(part1) - 1
    print(f'{F} × 2^{adjust}')

print("\n7. Round result\n")
if len(F.split(".")[1]) > 23:
    print("Round to only 23 fraction bits")
    F = F[:25]
    print(f'{F} (23 fraction bits)')
else:
    print("No need (fits in 23 bits)")

print("\n8.	Assemble exponent and fraction back into floating-point format\n")
print(f'S = {bin1[0]}')
print(f'E = {exp} + {adjust} = {exp + adjust} = {bin(exp + adjust)[2:]}(base 2)')
print(f'F = {F.split(".")[1]}')
ans = bin1[0] + bin(exp + adjust)[2:] + F.split(".")[1]
print(" ".join(re.findall("....?", ans)))
ans = hex(int(ans, 2))[2:].upper()
print("    ".join(re.findall(".", ans)))

print(f"\033[92mAnswer : Ox{ans}")
