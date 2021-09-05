def main():
    r, c = map(int, input().split())
    data = list()

    for i in range(r):
        row_data = list(map(int, input().split()))
        min_of_row = min(row_data)
        data.append(min_of_row)
    
    print(max(data))


if __name__ == '__main__':
    main()