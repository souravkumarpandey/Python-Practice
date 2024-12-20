def first_n_sum(n):
    sum =0
    i=1
    while(i<=n):
        sum+=i
        i+=1
    return sum

if __name__ == '__main__':
    n= int(input("enter the limit of n"))
    print(first_n_sum(n))