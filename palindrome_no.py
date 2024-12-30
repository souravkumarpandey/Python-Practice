def reversednumber(number):
    str_num = ""
    while number > 0:
        digit = number % 10

        str_num += str(digit)
        number //= 10
    reversed_number = int(str_num)
    return reversed_number

if __name__ == '__main__':
    number = int(input("enter the number to checkthe palindrome"))

    if number== reversednumber(number):
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
