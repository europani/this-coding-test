def main():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort(reverse=True)
    first = data[0]
    second = data[1]

    result = 0
    while 1:
        for i in range(k):
            result += first
            m-=1
            if m == 0:
                break
        result+=second
        m-=1
        if m == 0:
            break

    print(result)


if __name__ == '__main__':
    main()