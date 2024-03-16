if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    heigh = arr[0]
    for i in range(len(arr)):
        if arr[i] != heigh:
            print(arr[i])
            break;