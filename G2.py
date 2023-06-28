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