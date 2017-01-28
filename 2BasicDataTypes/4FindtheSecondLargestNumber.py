if __name__ == '__main__':
    n = int(raw_input())
    arr = set(map(int, raw_input().split()))
    arr.remove(max(arr))
    print max(arr)