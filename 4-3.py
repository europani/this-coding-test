def main():
    input_data = input()
    column = ord(input_data[0]) - ord('a') + 1
    row = int(input_data[1])

    move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)] 
    result = 0

    for i in move:
        move_row = row + i[0]   
        move_column = row + i[1]

        if move_row >0 and move_row < 9 and move_column >0 and move_column < 9:
            result +=1
    
    print(result)


if __name__ == '__main__':
    main()