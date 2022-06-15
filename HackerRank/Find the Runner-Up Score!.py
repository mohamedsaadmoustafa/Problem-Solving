if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Here we go!
    #print(max(sorted(set(arr))[:-1]))
    print(sorted(set(arr))[:-1][-1])
