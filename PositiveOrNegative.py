def positive_negstive(n):
    if n>0:
        return "Positive"
    elif n==0:
        return "No is zero"
    else:
        return "no is negative"

if __name__ == '__main__':
    n= int(input("Enter the input to check"))
    print(positive_negstive(n))


