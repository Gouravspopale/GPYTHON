 # python program to print message.
print(" HI GOURAV WELL COME TO PYTHON PROGRAM")

#python program to print sum of two numbers
a,b=10,5
print("Sum Of Two numbers",a+b)

# python program to print area and perimeter of square
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

import tkinter as tk

main = tk.Tk(className="  #STUDENT ID CARD#")
main.geometry("600x600")
main.configure(bg='white')

lable1=tk.Label(main,text="NAME:").grid(row=0,column=0)
txt1=tk.Entry(main).grid(row=0,column=1)

lable2=tk.Label(main,text="CLASS:").grid(row=1,column=0)
txt2=tk.Entry(main).grid(row=1,column=1)

lable3=tk.Label(main,text="DOB:").grid(row=2,column=0)
txt3=tk.Entry(main).grid(row=2,column=1)

lable4=tk.Label(main,text="AREA:").grid(row=3,column=0)
txt4=tk.Entry(main).grid(row=3,column=1)

lable5=tk.Label(main,text="PHONE NO:").grid(row=4,column=0)
txt5=tk.Entry(main).grid(row=4,column=1)

lable6=tk.Label(main,text="VALIDIYY OF ID CARD:").grid(row=5,column=0)
txt6=tk.Entry(main).grid(row=5,column=1)

btn6=tk.Button(main,text="submit").grid(row=6,column=1)


main.mainloop()
# lable1.grid(row=0,column=0)
# txt1.grid(row=0,column=1)

# lable2.grid(row=1,column=0)
# txt2.grid(row=1,column=1)

# lable3.grid(row=2,column=0)
# txt3.grid(row=2,column=1)

# lable4.grid(row=3,column=0)
# txt4.grid(row=3,column=1)

# lable5.grid(row=4,column=0)
# txt5.grid(row=4,column=1)

# lable6.grid(row=5,column=0)
# txt6.grid(row=5,column=1)
# btn6.grid(row=6,column=1)

# main.mainloop()