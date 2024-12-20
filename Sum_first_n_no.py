def first_n_sum(n):
    sum =0
    i=1
    while(i<=n):
        sum+=i
        i+=1
    return sum

def recurSum(n):
    if n==1:
        return 1
    return  n+recurSum(n-1)


if __name__ == '__main__':
    n= int(input("enter the limit of n"))
    print(recurSum(n))