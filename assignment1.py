#!/usr/bin/env python3

import tkinter as tk #this is just importing tkinter so that i can build the user interface
from tkinter import ttk


class BMIFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10") #10 px everywhere
        self.pack() #self variable makes sure that you can have several windows open at the same time with different values

        # Define float variables for text entry fields
        #add them as float variables!! and if else error: needs to be a number
        self.Height_feet = tk.IntVar() #variables can be shared across different parts of your programme
        self.Height_inch = tk.IntVar()
        self.Height_cm = tk.IntVar()
        self.Weight_st = tk.IntVar()
        self.Weight_lbs = tk.IntVar()
        self.Weight_kg = tk.IntVar()

        self.BMI = tk.IntVar()

        # Display the grid of components

        ttk.Label(self, text="Enter height:").grid(
            column=3, row=0, sticky=tk.E)

        ttk.Label(self, text="feet:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.Height_feet).grid(
            column=1, row=1)

        ttk.Label(self, text="inches:").grid(
            column=2, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.Height_inch).grid(
            column=3, row=1)

        ttk.Label(self, text="centimeters:").grid(
            column=4, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.Height_cm).grid(
            column=5, row=1)

        ttk.Label(self, text="Enter your weight:").grid(
            column=3, row=2, sticky=tk.E)

        ttk.Label(self, text="stones:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.Weight_st).grid(
            column=1, row=3)

        ttk.Label(self, text="pounds:").grid(
            column=2, row=3, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.Weight_lbs).grid(
            column=3, row=3)

        ttk.Label(self, text="Kg:").grid(
            column=4, row=3, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.Weight_kg).grid(
            column=5, row=3)

        ttk.Label(self, text="BMI:").grid(
            column=0, row=6, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.BMI,
                  state="readonly").grid(
            column=1, row=6)

        ttk.Button(self, text="Calculate BMI",
                   command=self.calculate_bmi).grid(
            column=1, row=7, sticky=tk.E)

        self.Imperial = tk.StringVar()
        ttk.Radiobutton(self, text="Select Imperial", variable=self.Type_Imperial, command=self.selected).grid(
            column=1, row=4)

        self.Metric = tk.StringVar()
        ttk.Radiobutton(self, text="Select Metric", variable=self.Type_Metric, command=self.selected).grid(
            column=2, row=4)

        #Add padding to all components
        for child in self.winfo_children(): #winfo = window info
            child.grid_configure(padx=5, pady=3)


    #if user selected Imperial, run this function

    def selected(self):
     if tk.StringVar() == Type_Imperial             #i don't understand how to

    Height_feet = float(self.Height_feet.get())
    Height_inch = float(self.Height_inch.get())
    Weight_st = float(self.Weight_st.get())
    Weight_lbs = float(self.Weight_lbs.get())

    Height_conversion = Height_feet * 30.48 + Height_inch * 2.54
    Weight_conversion = Weight_st * 6.5 + Weight_lbs * 0.45

    #BMI calculation formula
    def calculate_bmi(self):
        bmi = (self.Weight_conversion / pow(self.Height_conversion, 2))


    # Display the BMI in the text field
    self.BMI.set(bmi)


    #If statements that tells you your BMI range
    def bmi_category(self, bmi):

        if bmi <= 18.5:
            print('Your BMI is', bmi, 'which means you are underweight.')

        elif bmi > 18.5 and bmi < 25:
            print('Your BMI is', bmi, 'which means you are normal.')

        elif bmi > 25 and bmi < 30:
            print('Your BMI is', bmi, 'which means you are overweight.')

        elif bmi > 30:
            print('Your BMI is', bmi, 'which means you are obese.')

        else:
            print('There is an error with your input')


    #check values (example)
    '''if 0 < Height_cm < 300:
        self.Height_cm = Height_cm
    else: raise ValueError, "Invalid input for height", % Height_cm'''


    #run this if metric is selected in the button

    def selected(self):
     if self.Type_Metric == True

    Height_cm = float(self.Height_cm.get())
    Weight_kg = float(self.Weight_kg.get())

    # Calculate the BMI
    def calculate_bmi(self):
        bmi = (self.Weight_kg / pow(self.Height_cm, 2))


    # Display the BMI in the text field
        self.BMI.set(bmi)


    #If statements that tells you your BMI range

    def bmi_category(self, bmi):

        if bmi <= 18.5:
            print('Your BMI is', bmi, 'which means you are underweight.')

        elif bmi > 18.5 and bmi < 25:
            print('Your BMI is', bmi, 'which means you are normal.')

        elif bmi > 25 and bmi < 30:
            print('Your BMI is', bmi, 'which means you are overweight.')

        elif bmi > 30:
            print('Your BMI is', bmi, 'which means you are obese.')

        else:
            print('There is an error with your input')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BMI Calculator")
    BMIFrame(root) #if we take this out, the window will be blank (this is a constructor that does most of the work of creating the GUI)
    root.mainloop()
