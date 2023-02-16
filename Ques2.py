#write a recursive python function to print first N natural numbers in reverse order ?
def natural(n):
   if n>0:
    print(n)
    natural(n-1)
n=int(input("Enter how many natural numbers :"))
natural(n)
   
