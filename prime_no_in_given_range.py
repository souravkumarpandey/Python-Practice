def check_for_prime(number):

    if number < 0:
        print(number ,"is not prime")
    else:
        for i in range(2, number):
            if number % i == 0:
                print(number,"is not prime")
                break
            else:
                print(number," is prime")
                break

if __name__ == '__main__':
    start=int(input("Enter the starting number of the range"))
    end=int(input("enter the ending no of the range"))

    for num in range(start,end):
        check_for_prime(num)

