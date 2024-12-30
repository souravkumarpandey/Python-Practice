if __name__ == '__main__':
    number= int(input("enter the no to check"))
    if number<0:
        print("Number is not prime")
    else:
        for i in range (2,number):
            if number % i==0:
                print("number is not prime")
                break
            else:
                print("number is prime")
                break


