# if i enter 1 it have to give me the output of 3 times 
list_1=[1,1,1,25,25,46,67,88,88]
print(list_1)
x=int(input("enter a number : "))
count=0
for i in list_1:
    if i==x:
        count+=1
print(f"the given element {x} repated {count} times ")