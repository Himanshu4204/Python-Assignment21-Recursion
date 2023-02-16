# Write a recursive python function to print first N natural numbers.?
def natural(n):
    if n>0:
        natural(n-1)
        print(n)
n=int(input("Enter how many Natural Numbers you want :"))
natural(n)



