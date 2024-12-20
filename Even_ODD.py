def oddeven(n:int):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

if __name__=='__main__':
    n=int(input("enter the no. to check"))
    print(oddeven(n))