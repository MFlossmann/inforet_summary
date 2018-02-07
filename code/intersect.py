def intersect(list1, list2):
    i = 0  # The pointer in the first list.
    j = 0  # The pointer int the second list.
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return result
