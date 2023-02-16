#write a recursive python function to print squares of first N natural Numbers?
def square_natural(n):
    if n>0: 
        square_natural(n-1)
        print(n**2)
n=int(input("Enter how many numbers square you want :"))
square_natural(n)