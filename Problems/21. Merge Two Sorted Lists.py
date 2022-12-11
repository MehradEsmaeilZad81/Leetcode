# Actully, I solved the different problem, but I think it's the same, The only difference is that the main problem is on the leetcode.com with Linkedlist.

list1 = [int(num) for num in input().split()]
list2 = [int(num) for num in input().split()]

output = []


def MergeTwoSortedLists(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    j = 0
    i = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1
    if i == len(list1):
        output.extend(list2[j:])
    elif j == len(list2):
        output.extend(list1[i:])
    return output


print(MergeTwoSortedLists(list1, list2))
