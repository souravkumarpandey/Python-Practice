def gratestofSum(num1,num2):
    if num1>num2:
        return "num1 is greater"
    else:
        return "num2 is greater"

if __name__ == '__main__':
    num1=int(input("Enter the nums1"))
    num2=int(input("Enter the num2"))

    print(gratestofSum(num1,num2))