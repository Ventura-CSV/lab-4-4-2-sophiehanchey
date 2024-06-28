def main():
    
    while True:
        try:
            number = int(input('Please enter a numerical value: '))
        except:
            print('invalid input: Value Error')
            continue
        else:
            print(number)
            break
    
    return number


if __name__ == '__main__':
    main()
