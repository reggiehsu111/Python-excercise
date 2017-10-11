from tkinter import *
import math

class calc():
    def getandreplace(self):
        """replace x with * and ÷ with /"""
        self.expression = self.e.get()
        self.newtext=self.expression.replace(self.newdiv,'/')
        self.newtext=self.newtext.replace('x','*')

    def equals(self):
        """when the equal button is pressed"""

        self.getandreplace()
        try:
            self.value= eval(self.newtext) #evaluate the expression using the eval function
        except SyntaxError or NameErrror:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

    def squareroot(self):
        """squareroot method"""

        self.getandreplace()
        try:
            self.value= eval(self.newtext) #evaluate the expression using the eval function
        except SyntaxError or NameErrror:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.sqrtval=math.sqrt(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.sqrtval)

    def square(self):
        """square method"""

        self.getandreplace()
        try:
            self.value= eval(self.newtext) #evaluate the expression using the eval function
        except SyntaxError or NameErrror:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.sqval=math.pow(self.value,2)
            self.e.delete(0,END)
            self.e.insert(0,self.sqval)

    def clearall(self):
        """when clear button is pressed,clears the text input area"""
        self.e.delete(0,END)

    def clear1(self):
        self.txt=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)

    def action(self,argi):
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END,argi)

    def __init__(self,master):
        """Constructor method"""
        self.e = Entry(master)
        self.e.grid(row=0,column=0,columnspan=6,pady=3)
        self.e.focus_set() #Sets focus on the input text area
        self.newdiv='÷'

        #Generating Buttons
        Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
        Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
        Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
        Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
        Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
        Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
        Button(master,text="÷",width=3,command=lambda:self.action('÷')).grid(row=1, column=3)
        Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
        Button(master,text="7",width=3,command=lambda:self.action(7)).grid(row=1, column=0)
        Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
        Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
        Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
        Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
        Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
        Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
        Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
        Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
        Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
        Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
        Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
        Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
        Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
        Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)
class vector():
    def __init__(self,master):

        self.button=Button(master,text="Get from Cal",command=self.getvector)
        self.button.grid(row=2)

        x1=Label(master,text="x1").grid(column=1,row=1)
        self.ex1=Entry(master)
        self.ex1.grid(column=2,row=1)
        x2=Label(master,text="x2").grid(column=3,row=1)
        self.ex2=Entry(master)
        self.ex2.grid(column=4,row=1)
        x3=Label(master,text="x3").grid(column=5,row=1)
        self.ex3=Entry(master)
        self.ex3.grid(column=6,row=1)
    def getvector(self):
        Vector=(self.ex1.get(),self.ex2.get(),self.ex3.get())
        print(Vector)


#Main
root = Tk()
root.title("mix Caculator")
#root.geometry("500x500")
frame1=Frame(root,width=200,height=500)
#frame1.grid_columnconfigure(4, minsize=100)
frame2=Frame(root)
frame3=Frame(root)
calculator=calc(frame1) #object instantiated
vector1=vector(frame2)
vector2=vector(frame3)
frame1.pack(side=RIGHT,fill=BOTH,expand=YES)
frame2.pack(side=LEFT,fill=BOTH,expand=YES)
frame3.pack(fill=BOTH,expand=YES)
root.mainloop()