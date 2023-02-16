# write a recursive python function to print a number in reverse order?
def reverse_order(n):
    if n<10:
        print(n)
    else:
        print(n%10,end="")
        reverse_order(n//10)
n=int(input("Enter a Number :"))
reverse_order(n)
