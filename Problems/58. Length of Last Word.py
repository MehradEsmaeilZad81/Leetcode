s = input()


def LengthOfLastWord(s):
    s = s.split()
    if not len(s):
        return 0
    else:
        return len(s[-1])


print(LengthOfLastWord(s))
