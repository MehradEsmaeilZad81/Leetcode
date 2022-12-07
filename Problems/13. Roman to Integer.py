s = input()


def romanToInt(s):
    sum = 0
    for i in range(len(s)):
        if s[i] == 'I':
            if i < len(s)-1 and (s[i+1] == 'V' or s[i+1] == 'X'):
                sum -= 1
            else:
                sum += 1
        elif s[i] == 'V':
            sum += 5
        elif s[i] == 'X':
            if i < len(s)-1 and (s[i+1] == 'L' or s[i+1] == 'C'):
                sum -= 10
            else:
                sum += 10
        elif s[i] == 'L':
            sum += 50
        elif s[i] == 'C':
            if i < len(s)-1 and (s[i+1] == 'D' or s[i+1] == 'M'):
                sum -= 100
            else:
                sum += 100
        elif s[i] == 'D':
            sum += 500
        elif s[i] == 'M':
            sum += 1000
    return sum

print(romanToInt(s))