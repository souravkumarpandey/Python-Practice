if __name__ == '__main__':
    number= int(input("Enter the number to reverser"))
    str_num=""
    while number>0:
        digit=number%10

        str_num+=str(digit)
        number//=10
    reversed_number=int(str_num)
    print(reversed_number)