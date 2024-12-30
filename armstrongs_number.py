def armstrongs(number):
    cpy_number=number
    sum= 0
    lenn=len(str(number))
    while(number>0):
        digit=number%10
        sum+=digit**lenn
        number//=10
    print(sum)
    if sum ==cpy_number:
        print("number is armstrong")
    else:
        print("number is not armstrongs")

if __name__ == '__main__':
    number =int(input("Enter the number to check "))
    armstrongs(number)