#  importing the libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import pickle   
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__() # inherits from the Tk class

        # configure the root window
        self.title("Heart Disease Prediction APP  GUI")
        self.geometry("900x600")

        # configuring style 
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", font = ("JetBrains Mono", 10))
        self.style.configure("Input.TLabel", font = ("consolas", 9))

        # heading and sub heading
        self.label = ttk.Label(self, text = "Model GUI", font = ("consolas", 30)).grid(row = 0, column = 1, pady = 0)
        self.sub_heading = ttk.Label(self,text = "Type the following  entries", font = ("consolas", 15)).grid(row = 2, column = 1, pady = (5,20))

        # submit button
        self.button = ttk.Button(self, text='Submit' , width = 10)
        self.button['command'] = self.button_clicked
        self.button.grid(row = 16, column = 2 , pady = 10)

        self.my_entries = [] # user entries

        # for validation 
        self.vcmd = (self.register(self.on_valid))
        self.ivcmd = (self.register(self.on_invalid))

        #Column 1 
        self.col_1_label=ttk.Label(self,text="age")
        self.col_1_label.grid(row=3,column=1,sticky=tk.W)
        self.col_1_var=tk.DoubleVar()
        self.col_1_entry=tk.Entry(self,width=16,textvariable=self.col_1_var)
        self.col_1_entry.grid(row=3,column=2)
        self.col_1_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_1_label.cget("text")))
    #     #Column 2
        self.col_2_label=ttk.Label(self,text="gender")
        self.col_2_label.grid(row=4,column=1,sticky=tk.W)
        self.col_2_var=tk.DoubleVar()
        self.col_2_helpmsg = ttk.Label(self, text = "[ 0 for male and 1 for female ]").grid(row = 4, column = 0, padx = 10)
        self.col_2_entry=tk.Checkbutton(self,width=16,textvariable=self.col_2_var,onvalue=1.0, offvalue=0.0,  command=lambda:self.toggle(self.col_2_var))
    #    use state method ,https://stackoverflow.com/questions/4236910/getting-checkbutton-state#:~:text=If%20you%20use%20the%20new,checkbutton%20states%20without%20assigning%20variables.&text=To%20set%20the%20state%20in,%5D)%20%23%20check%20the%20checkbox%20chk.
        self.col_2_entry.grid(row=4,column=2)

        #Column 3
        self.col_3_label=tk.Label(self,text="cp")
        self.col_3_label.grid(row=5,column=1,sticky=tk.W)
        self.col_3_var=tk.DoubleVar()
        self.col_3_entry=tk.Entry(self,width=16,textvariable=self.col_3_var)
        self.col_3_entry.grid(row=5,column=2)
        self.col_3_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_3_label.cget("text")))
        
        #Column 4
        self.col_4_label=ttk.Label(self,text="trestbps")
        self.col_4_label.grid(row=6,column=1,sticky=tk.W)
        self.col_4_var=tk.DoubleVar()
        self.col_4_entry=tk.Entry(self,width=16,textvariable=self.col_4_var)
        self.col_4_entry.grid(row=6,column=2)
        self.col_4_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_4_label.cget("text")))

        #Column 5
        self.col_5_label=ttk.Label(self,text="chol")
        self.col_5_label.grid(row=7,column=1,sticky=tk.W)
        self.col_5_var=tk.DoubleVar()
        self.col_5_entry=tk.Entry(self,width=16,textvariable=self.col_5_var)
        self.col_5_entry.grid(row=7,column=2)
        self.col_5_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_5_label.cget("text")))

        #Column 6
        self.col_6_label=ttk.Label(self,text="fbs")
        self.col_6_label.grid(row=8,column=1,sticky=tk.W)
        self.col_6_var=tk.DoubleVar()
        self.col_6_entry=tk.Entry(self,width=16,textvariable=self.col_6_var)
        self.col_6_entry.grid(row=8,column=2)
        self.col_6_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_6_label.cget("text")))

        #Column 7
        self.col_7_label=ttk.Label(self,text="restecg")
        self.col_7_label.grid(row=9,column=1,sticky=tk.W)
        self.col_7_var=tk.DoubleVar()
        self.col_7_entry=tk.Entry(self,width=16,textvariable=self.col_7_var)
        self.col_7_entry.grid(row=9,column=2)
        self.col_7_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_7_label.cget("text")))

        #Column 8
        self.col_8_label=ttk.Label(self,text="thalach")
        self.col_8_label.grid(row=10,column=1,sticky=tk.W)
        self.col_8_var=tk.DoubleVar()
        self.col_8_entry=tk.Entry(self,width=16,textvariable=self.col_8_var)
        self.col_8_entry.grid(row=10,column=2)
        self.col_8_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_8_label.cget("text")))

        #Column 9
        self.col_9_label=ttk.Label(self,text="exang")
        self.col_9_label.grid(row=11,column=1,sticky=tk.W)
        self.col_9_var=tk.DoubleVar()
        self.col_9_entry=tk.Entry(self,width=16,textvariable=self.col_9_var)
        self.col_9_entry.grid(row=11,column=2)
        self.col_9_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_9_label.cget("text")))

        #Column 10
        self.col_10_label=ttk.Label(self,text="oldpeak")
        self.col_10_label.grid(row=12,column=1,sticky=tk.W)
        self.col_10_var=tk.DoubleVar()
        self.col_10_entry=tk.Entry(self,width=16,textvariable=self.col_10_var)
        self.col_10_entry.grid(row=12,column=2)
        self.col_10_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_10_label.cget("text")))

        #Column 11
        self.col_11_label=ttk.Label(self,text="slope")
        self.col_11_label.grid(row=13,column=1,sticky=tk.W)
        self.col_11_var=tk.DoubleVar()
        self.col_11_entry=tk.Entry(self,width=16,textvariable=self.col_11_var)
        self.col_11_entry.grid(row=13,column=2)
        self.col_11_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_11_label.cget("text")))

        #Column 12
        self.col_12_label=ttk.Label(self,text="ca")
        self.col_12_label.grid(row=14,column=1,sticky=tk.W)
        self.col_12_var=tk.DoubleVar()
        self.col_12_entry=tk.Entry(self,width=16,textvariable=self.col_12_var)
        self.col_12_entry.grid(row=14,column=2)
        self.col_12_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_12_label.cget("text")))

        #Column 13
        self.col_13_label=ttk.Label(self,text="thal")
        self.col_13_label.grid(row=15,column=1,sticky=tk.W)
        self.col_13_var=tk.DoubleVar()
        self.col_13_entry=tk.Entry(self,width=16,textvariable=self.col_13_var)
        self.col_13_entry.grid(row=15,column=2)
        self.col_13_entry.config(validate='focusout', validatecommand=(self.vcmd, '%P'), invalidcommand=(self.ivcmd,self.col_13_label.cget("text")))
    
    # toggle the value of checkbox
    def toggle(self, var):
        var.set(not var.get())

     # callback when data typed is valid
    def on_valid(self,value):
        try :
            value = float(value)     
            return True       
        except :
            return False

    # callback when data typed is not valid
    def on_invalid(self, label_text):
        return messagebox.showerror('Error', ('invalid data for ' + label_text +  ' only integers or decimals accepted.'))

    # submit button function 
    def button_clicked(self):
        try :
            self.my_entries = [self.col_1_var.get(), self.col_2_var.get(), self.col_3_var.get(), self.col_4_var.get(), self.col_5_var.get(), self.col_6_var.get(), self.col_7_var.get(), self.col_8_var.get(), self.col_9_var.get(), self.col_10_var.get(), self.col_11_var.get(), self.col_12_var.get(), self.col_13_var.get()]
        except :
            return messagebox.showerror("Error", "Invalid values , try again")
        else :
            messagebox.showinfo("Success", "Valid Entries")
            self.res = messagebox.askyesno("Proceed ?", "Go ahead with modelling this data ?")
            if(self.res == True):
                self.run_model(self.my_entries)
            self.col_1_var.set(0.0), self.col_2_var.set(0.0), self.col_3_var.set(0.0), self.col_4_var.set(0.0), self.col_5_var.set(0.0), self.col_6_var.set(0.0), self.col_7_var.set(0.0), self.col_8_var.set(0.0), self.col_9_var.set(0.0), self.col_10_var.set(0.0), self.col_11_var.set(0.0), self.col_12_var.set(0.0), self.col_13_var.set(0.0)
    
    # run the model on the validated array of data
    def run_model(self, entry_list):
        # run the model , show the output using a label 
        print(entry_list)
        entry_list = np.array(entry_list).reshape(1,13)
        with open("model", "rb") as f:
            model = pickle.load(f)
            print(model.predict(entry_list))
            if(model.predict(entry_list) == 1):
                return messagebox.showinfo("Info", "You do not have the heart disease.")
            else:
                return messagebox.showinfo("Info", "You do  have the heart disease.")

if __name__ == "__main__":
    app = App()
    app.mainloop()