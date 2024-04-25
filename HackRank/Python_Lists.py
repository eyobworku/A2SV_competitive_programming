if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        inp = input().split()
        if inp[0] == 'insert':
            arr.insert(int(inp[1]),int(inp[2]))
        elif inp[0] == 'print':
            print(arr)
        elif inp[0] == 'remove':
            arr.remove(int(inp[1]))
        elif inp[0] == 'append':
            arr.append(int(inp[1]))
        elif inp[0] == 'sort':
            arr.sort()
        elif inp[0] == 'pop':
            arr.pop()
        elif inp[0] == 'reverse':
            arr.reverse()
                
