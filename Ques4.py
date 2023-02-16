#4. Write a recursive python function to print first N odd natural numbers in reverse order?
def odd_reverse(n):
    if n>0:
        print(n+(n-1),end=' ')
        odd_reverse(n-1)     
n=int(input("Enter how many odd Numbers you want :"))
odd_reverse(n)
