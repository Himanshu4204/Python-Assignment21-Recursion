#write a recursive python function to print first N Even Natural numbers in reverse order?
def Even_reverse(n):
    if n>0:
        print(2*n)
        Even_reverse(n-1)
n=int(input("Enter how many numbers you want :"))
Even_reverse(n)
