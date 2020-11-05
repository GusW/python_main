def binary_search(items, desired_item, start=0, end=None):
    end = end or len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        return pos
    elif desired_item > items[pos]:
        return binary_search(items, desired_item, start=(pos + 1), end=end)
    else:
        return binary_search(items, desired_item, start=start, end=pos)


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum -= 1

    return alist


def quickSort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = quickSort([x for x in inlist[1:] if x < pivot])
        greater = quickSort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


def merge_sort(inlist):
    from copy import deepcopy

    new_list = deepcopy(inlist)
    if len(new_list) > 1:
        mid = len(new_list) // 2
        left = new_list[:mid]
        right = new_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                new_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                new_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            new_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            new_list[k] = right[j]
            j += 1
            k += 1

    return new_list


someList = [200, 20, 30, 210, 40, 90, 50, 215, 60, 70, 80, 100, 110]


print(f'BubbleSort == {shortBubbleSort(someList)}')
print(f'merge_sort == {merge_sort(someList)}')
print(f'QuickSort == {quickSort(someList)}')
print(f'BinarySearch == {binary_search(quickSort(someList), 215)}')


def solution(A, B):
    res = ''
    major, majorLetter = (range(A), 'a') if A > B else (range(B), 'b')
    minor, minorLetter = (range(B), 'b') if majorLetter == 'a' else (range(A), 'a')
    while len(major) or len(minor):
        for i in major:
            if i < 2:
                res += majorLetter
                major = range(len(major)-1)
            else:
                i = 1
                break

        for j in minor:
            if j < 2:
                res += minorLetter
                minor = range(len(minor)-1)
            else:
                j = 1
                break

    return res


print(solution(3, 3))
print(solution(1, 4))


def solution2(T):
    cakeTypeCounter = {}
    for i in set(T):
        cakeTypeCounter[i] = T.count(i)

    giveAwayCakes = 0
    reverseCakeList = sorted(cakeTypeCounter.items(), key=lambda x: x[1], reverse=True)
    while giveAwayCakes < len(T)/2:
        for k, v in reverseCakeList:
            if v > len(T)/2:
                cakeTypeCounter[k] = v - len(T)/2
                giveAwayCakes += len(T)/2
            elif v == len(T)/2:
                cakeTypeCounter[k] = (v - len(T)/2) + 1
                giveAwayCakes += (len(T)/2) - 1
            elif v > 1:
                cakeTypeCounter[k] = int(v/2)
                giveAwayCakes += (v - cakeTypeCounter[k])
            else:
                if sum([v for v in cakeTypeCounter.values()]) > len(T)/2:
                    cakeTypeCounter[k] = v - 1

                giveAwayCakes += 1

    print(cakeTypeCounter)
    return len([v for _, v in cakeTypeCounter.items() if v > 0])


print(solution2([3, 4, 7, 7, 6, 6]))

print(solution2([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]))
