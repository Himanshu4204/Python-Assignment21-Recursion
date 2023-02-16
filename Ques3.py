#3. Write a recursive python function to print first N odd natural numbers?
def odd_natural(n):
    if n>1:
        odd_natural(n-1)
    if n%2!=0:
        print(n)
n=int(input("Enter how many odd numbers you want :"))
odd_natural(2*n)