#Write a recursive python function  to print first N multiples of a given number >
def Multiples(a,n):
    if n>0:
        Multiples(a,n-1)
        print(a*n)
a=int(input("Enter number you want multiple :"))
n=int(input("Enter How Many multiples you want :"))
Multiples(a,n)