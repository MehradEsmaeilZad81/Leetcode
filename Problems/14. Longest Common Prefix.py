strs = [str for str in input().split()]


def longestCommonPrefix(strs):
    if strs:
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for str in strs:
                if str[i] != char:
                    return shortest[:i]
        return shortest
    else:
        return ""


print(longestCommonPrefix(strs))
