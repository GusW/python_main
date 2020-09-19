def binary_search(items, desired_item, start=0, end=None):
    if end is None:
        end = len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        return pos
    elif desired_item > items[pos]:
        return binary_search(items, desired_item, start=(pos + 1), end=end)
    else:  # desired_item < items[pos]:
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
        passnum = passnum-1

    return alist


def quickSort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = quickSort([x for x in inlist[1:] if x < pivot])
        greater = quickSort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


someList = [200, 20, 30, 210, 40, 90, 50, 215, 60, 70, 80, 100, 110]

print(shortBubbleSort(someList))

print(quickSort(someList))

print(binary_search(quickSort(someList), 215))


def solution(A, B):
    # write your code in Python 3.6
    res = ''
    # import pdb; pdb.set_trace()
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
    # giveAwaySize = T/2
    # import pdb; pdb.set_trace()
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
                # retainedCakes += len(T)/2
            elif v == len(T)/2:
                cakeTypeCounter[k] = (v - len(T)/2) + 1
                giveAwayCakes += (len(T)/2) - 1
                # retainedCakes += len(T)/2 + 1
            elif v > 1:
                cakeTypeCounter[k] = int(v/2)
                giveAwayCakes += (v - cakeTypeCounter[k])
                # retainedCakes +=
            else:
                if sum([v for v in cakeTypeCounter.values()]) > len(T)/2:
                    cakeTypeCounter[k] = v - 1

                giveAwayCakes += 1

    print(cakeTypeCounter)
    return len([v for _, v in cakeTypeCounter.items() if v > 0])


print(solution2([3, 4, 7, 7, 6, 6]))

print(solution2([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]))
