def resSum(sum,num1,num2):
    if num1>num2:
        return sum

    return num1+resSum(sum,num1+1,num2)



if __name__ == '__main__':
    num1 = int(input("Enter the first no"))
    num2= int(input("Enter the second no of the range"))
    sum=0
    print(resSum(sum,num1,num2))

