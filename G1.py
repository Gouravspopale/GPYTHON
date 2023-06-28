# python program to print message.
print(" HI GOURAV WELL COME TO PYTHON PROGRAM")

#python program to print sum of two numbers
a,b=10,5
print("Sum Of Two numbers",a+b)

# python program to print area and perimeter of square.
a=5 
area=(a*a)
peri=(a*4)
print("\nArea of Square",area,"\nperi of Square",peri)

#python program to print area and perimeter of Rectangle
l,b=5,3
area=(l*b)
peri=2*(l+b)
print("\nArea of Rectangle",area,"\nperi of Rectangle",peri)

#python program to print area and perimeter of Circle
r=7
area=(7*7)
peri=(2*3.14*7)
print("\nArea of Circle",area,"\nperi of Circle",peri)

# program to print Even and Odd number

n=10
if(n%2==0):
    print("The Given Value Is Even",n)
else:
    print("The Given Value Is Odd",n)

#program to find Positive and Negative values 

n=7
if(n>0):
    print("The Given Value Is  Positive",n)
else:
     print("The Given Value Is Negative",n)   

# program to find Simple intrest

p,t,r=12000,4,3
si=p*(t*r)/100
print("SiMPLE INTREST",si)

#program to find compund  intrest

p,t,r=5000,2,5.4
a=p*(1+(r/100))*t
print("COMPOUND INTREST",a)

# program to find Swap of number

p,q=10,5
p,q=q,p
print("Swap of p",p)