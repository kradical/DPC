print("Calculate the determinant of a 2x2 matrix!")
print("input format A B C D =\nA B\nC D")
print("input format A B C D E F G H I =\nA B C\nD E F\nG H I")
s = ""
while True:
    if s == "exit":
        break
    s = input("input (enter exit to quit): ")
    if s == "exit":
        break
    s = s.split()
    s = list(map(int, s))

    if len(s) is 4:
        result = s[0]*s[3]-s[2]*s[1]
        print("Determinant of entered matrix = " + str(result))
        continue
    if len(s) is 9:
        result = s[0]*s[4]*s[8]+s[1]*s[5]*s[6]+s[2]*s[3]*s[7]-s[6]*s[4]*s[2]-s[7]*s[5]*s[0]-s[8]*s[3]*s[1]
        print("Determinant of entered matrix = " + str(result))
        continue
    else:
        s = input("incorrect number of inputs try again:").split()
        continue

