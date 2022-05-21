import heapq  # implemented as min heap


def solution1(arr, k):
    arr.sort(reverse=True)  # O(T) NlogN
    return arr[k-1]         # O(S) 1


def solution2(arr, k):
    # multiplying by -1 to transform min heap into max heap
    arr = [-el for el in arr]   # O(N)
    heapq.heapify(arr)          # O(N)
    for _ in range(1, k):       # O(k)
        heapq.heappop(arr)      # O(logN)

    return -heapq.heappop(arr)  # O(logN)


if __name__ == "__main__":
    arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    k = 4
    print(solution1(arr, k))
    print(solution2(arr, k))
