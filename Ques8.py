#Write a recursive python function to print cubes of first N natural Numbers?
def cube_natural(n):
    if n>0:
        cube_natural(n-1)
        print(n**3)
n=int(input("Enter how many numbers cube you want :"))
cube_natural(n)