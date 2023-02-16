# write a recursive python function to print first N Even natural Numbers?
def natural_Even(n):
    if n>0:
        natural_Even(n-1)
        print(2*n)
n=int(input("Enter how many Even Numbers you want :"))
natural_Even(n)