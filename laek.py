from st import Leaky_stack



size=int(input("Enter size value = "))
l=Leaky_stack(size)

n=int(input("how many values you want to push = "))
for i in range(n):
    l.push(input("enter value="))
    l.display()