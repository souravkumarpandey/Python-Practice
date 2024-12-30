if __name__ == '__main__':
    number =int(input("Enter the number to check"))

    sum=0
    while number>0:
        digit=number%10
        sum+=digit
        number//=10
    print(sum)

